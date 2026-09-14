#!/usr/bin/env python3
"""Convert generated scene art into the form the catalog ships.

    ./catalog/prepare-images.py <input-dir>

Input:  one image per scene, named <scene-id>.<jpg|jpeg|png|webp>, any resolution.
Output: catalog/scenes/<scene-id>.webp, short edge 1600px, WebP q82.

The ONLY pixel operations are a proportional downscale and the WebP re-encode. Images are never
cropped (screens vary — phones, tablets, foldables — so framing is the app's business at runtime)
and never blurred (the app blurs at 8dp itself; blurring twice would just destroy detail).

Renaming a .jpg to .webp does NOT convert it — the bytes stay JPEG and the size benefit is lost.
This does a real re-encode.

It does compute one piece of metadata. Scenes render blurred under a dark overlay behind body
text, and a bright sky can leave that text below WCAG AA. Each scene is simulated exactly as the
reader sees it, and the minimum overlay opacity that keeps text legible is written into the
manifest as `overlayAlpha`. The image itself is left alone, so the decision stays adjustable: if
the text colour or default overlay ever changes, re-run this rather than re-exporting art.

Requires Pillow:  pip3 install Pillow
"""

from __future__ import annotations

import json
import os
import sys
from PIL import Image, ImageFilter

SHORT_EDGE = 1600
QUALITY = 82

# Must mirror ReaderScreen: Modifier.blur(8.dp) over BookPageBackgroundDark at 65%,
# with BookPageTextDark on top.
TEXT_RGB = (0xCF, 0xCF, 0xCF)
OVERLAY_RGB = (0x1A, 0x1C, 0x1E)
OVERLAY_ALPHA = 0.65
BLUR_PX_AT_3X = 24
PHONE_W, PHONE_H = 1080, 2340

MIN_CONTRAST = 4.5      # WCAG AA for body text
MAX_OVERLAY_ALPHA = 0.88  # past this the scene is more overlay than art; warn instead


def _linear(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb) -> float:
    r, g, b = (_linear(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def _blurred_for_measurement(im: Image.Image) -> Image.Image:
    """Simulate the reader's view for measurement only — never saved.

    Centre-cropping to a phone here is a worst-case probe, not a framing decision: the phone
    aspect keeps the least of the frame, so a scene that passes here passes on wider screens too.
    """
    scale = max(PHONE_W / im.width, PHONE_H / im.height)
    up = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    left, top = (up.width - PHONE_W) // 2, (up.height - PHONE_H) // 2
    crop = up.crop((left, top, left + PHONE_W, top + PHONE_H))
    return crop.filter(ImageFilter.GaussianBlur(BLUR_PX_AT_3X))


def worst_region_contrast(blurred: Image.Image, alpha: float) -> float:
    """Contrast against the brightest 5% of the frame, where light text suffers most."""
    final = Image.blend(blurred, Image.new("RGB", blurred.size, OVERLAY_RGB), alpha)
    tiles = list(final.resize((24, 52)).getdata())
    tiles.sort(key=luminance, reverse=True)
    worst = tiles[: max(1, len(tiles) // 20)]
    avg = tuple(sum(t[i] for t in worst) // len(worst) for i in range(3))
    return contrast(TEXT_RGB, avg)


def required_overlay_alpha(im: Image.Image):
    """Minimum overlay opacity keeping text at MIN_CONTRAST. Returns (alpha, achieved)."""
    blurred = _blurred_for_measurement(im)
    alpha = OVERLAY_ALPHA
    achieved = worst_region_contrast(blurred, alpha)
    while achieved < MIN_CONTRAST and alpha < MAX_OVERLAY_ALPHA:
        alpha = round(alpha + 0.01, 2)
        achieved = worst_region_contrast(blurred, alpha)
    return alpha, achieved


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: prepare-images.py <input-dir>", file=sys.stderr)
        return 64
    input_dir = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(here, "manifest.json")
    out_dir = os.path.join(here, "scenes")

    if not os.path.isdir(input_dir):
        print(f"error: no such directory: {input_dir}", file=sys.stderr)
        return 66
    if not os.path.isfile(manifest_path):
        print(f"error: manifest not found: {manifest_path}", file=sys.stderr)
        return 66
    os.makedirs(out_dir, exist_ok=True)

    sources = sorted(
        f for f in os.listdir(input_dir)
        if os.path.splitext(f)[1].lower() in (".jpg", ".jpeg", ".png", ".webp")
    )
    if not sources:
        print(f"error: no images found in {input_dir}", file=sys.stderr)
        return 66

    print(f"  {'scene':<26}{'in':>8}{'out':>7}  {'overlay':<15}{'dim':<12}{'contrast':>9}")
    print(f"  {'-' * 76}")

    warnings = []
    overlay_alpha = {}
    for name in sources:
        scene_id = os.path.splitext(name)[0]
        src_path = os.path.join(input_dir, name)
        im = Image.open(src_path).convert("RGB")

        if im.width > im.height:
            warnings.append(
                f"{scene_id}: landscape ({im.width}x{im.height}); scenes are centre-cropped on a "
                f"portrait screen so the sides will be lost. Portrait 2:3 is preferred."
            )

        scale = SHORT_EDGE / min(im.width, im.height)
        im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)

        alpha, achieved = required_overlay_alpha(im)
        overlay_alpha[scene_id] = alpha
        note = "" if alpha == OVERLAY_ALPHA else f"overlay {alpha:.2f}"
        if achieved < MIN_CONTRAST:
            warnings.append(
                f"{scene_id}: only {achieved:.1f}:1 even at overlay {alpha:.2f} — the source is too "
                f"bright. Regenerate it darker or with less open sky."
            )

        out_path = os.path.join(out_dir, f"{scene_id}.webp")
        im.save(out_path, "WEBP", quality=QUALITY, method=6)

        print(
            f"  {scene_id:<26}"
            f"{os.path.getsize(src_path)//1024:>7}K"
            f"{os.path.getsize(out_path)//1024:>6}K"
            f"  {note:<15}"
            f"{f'{im.width}x{im.height}':<12}"
            f"{achieved:>7.1f}:1"
        )

    for w in warnings:
        print(f"\n  warning: {w}", file=sys.stderr)

    # Write the measured overlay back into the manifest so the app applies it at runtime and the
    # art stays untouched.
    manifest = json.load(open(manifest_path))
    for scene in manifest["scenes"]:
        alpha = overlay_alpha.get(scene["id"])
        if alpha is None or alpha == OVERLAY_ALPHA:
            scene.pop("overlayAlpha", None)
        else:
            scene["overlayAlpha"] = alpha
    with open(manifest_path, "w") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    ids = {s["id"] for s in manifest["scenes"]}
    have = {f[:-5] for f in os.listdir(out_dir) if f.endswith(".webp")}
    missing, extra = sorted(ids - have), sorted(have - ids)

    print()
    if missing:
        print("  MISSING (in manifest, no image):")
        for i in missing:
            print(f"    {i}")
    if extra:
        print("  UNREFERENCED (image present, not in manifest — check the filename):")
        for i in extra:
            print(f"    {i}")
    if not missing and not extra:
        print(f"  OK: all {len(ids)} manifest scenes have a matching image.")

    total = sum(
        os.path.getsize(os.path.join(out_dir, f))
        for f in os.listdir(out_dir) if f.endswith(".webp")
    )
    print(f"  catalog image payload: {total/1024:.0f} KB")
    return 1 if (missing or extra) else 0


if __name__ == "__main__":
    sys.exit(main())
