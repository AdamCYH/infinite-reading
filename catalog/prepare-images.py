#!/usr/bin/env python3
"""Convert generated scene art into the form the catalog ships.

    ./catalog/prepare-images.py <input-dir>

Input:  one image per scene, named <scene-id>.<jpg|jpeg|png|webp>, any resolution.
Output: catalog/scenes/<scene-id>.webp, short edge at most 1600px, WebP q82.

With --measure-only the input directory is optional and defaults to catalog/scenes: no image is
written, and only the manifest's measured values are recomputed. That is the mode to use when
SCENE_BLUR_RADIUS, the scrim, the text colour or the grade changes, because the masters live
outside the repo and the published art is the pixels the app actually loads anyway.

The ONLY pixel operations are a proportional downscale and the WebP re-encode. Images are never
cropped (screens vary — phones, tablets, foldables — so framing is the app's business at runtime)
and never blurred (the app blurs at 2.5dp itself; blurring twice would just destroy detail).

Renaming a .jpg to .webp does NOT convert it — the bytes stay JPEG and the size benefit is lost.
This does a real re-encode.

The overlay is a legibility guarantee, not a darkening effect, so it is searched from a floor
rather than from a fixed default and only rises when the text needs it.

It does compute two pieces of metadata, both written into the manifest and neither baked into
the art, so both stay adjustable without re-exporting anything.

`overlayAlpha` — scenes render blurred under a dark scrim behind body text, and a bright sky can
leave that text below WCAG AA. Each scene is simulated exactly as the reader sees it and the
minimum scrim that keeps text legible is recorded.

`saturation` — blur averages colour toward grey, so a muted scene renders neutral. Scenes that
measure below CHROMA_FLOOR once blurred get a lift, capped at MAX_SATURATION; everything already
colourful enough is left at 1.0 and carries no value at all. A blanket multiplier would ruin the
scenes that are already saturated, which is why this is measured per scene.

Requires Pillow:  pip3 install Pillow
"""

from __future__ import annotations

import json
import os
import re
import sys
from PIL import Image, ImageEnhance, ImageFilter

SHORT_EDGE = 1600
QUALITY = 82

# Bumped when the shape of the file changes, not when the numbers do. Clients ignore keys they do
# not know, so this is for humans and for tooling rather than a gate.
SCHEMA_VERSION = 2

# Must mirror the reader: SCENE_BLUR_RADIUS, then the grade in SceneGrade.kt, with
# BookPageTextDark on top. OVERLAY_RGB is now only the veil shown before a scene has loaded.
TEXT_RGB = (0xCF, 0xCF, 0xCF)
OVERLAY_RGB = (0x1A, 0x1C, 0x1E)

OVERLAY_ALPHA = 0.65

# --- render profiles -------------------------------------------------------------------------
#
# A profile id names the WHOLE contract a measured number belongs to: the scrim maths AND the
# constants it was measured against. Change the blur radius or the ambient floor and the old
# numbers stop being valid, so that is a NEW profile id, not an edit to an existing one.
#
# Every profile is measured on every run, so the projections cannot drift apart - which is what
# went wrong before this existed: `overlayAlpha` was recomputed for a multiply scrim while the
# released app was still lerping, and 99 of 100 scenes fell under WCAG AA.
#
# `calibration` is published so the contract is visible in the file itself, and
# check_calibration_immutable() refuses to change one that has already shipped.
PROFILES = {
    "scrim-lerp-1": {
        "summary": "scrim lerped toward overlayColor; app 1.2 and earlier",
        "mode": "lerp",
        "saturation": False,
        "calibration": {
            "blurDp": 5.0,
            "textColor": "#CFCFCF",
            "overlayColor": "#1A1C1E",
            "minContrast": 4.5,
        },
        "defaults": {"scrim": 0.65},
        "minScrim": 0.45,
        # Frozen: app 1.2 is in the field reading these. A re-run keeps whatever was published as
        # long as it still clears minContrast, so boundary noise between runs - PIL versions,
        # float rounding - can never churn numbers that are already in users' hands.
        "frozen": True,
    },
    "scrim-multiply-1": {
        "summary": "scrim multiplied toward ambientColor, per-scene saturation; app 1.3+",
        "mode": "multiply",
        "saturation": True,
        "calibration": {
            "blurDp": 2.5,
            "textColor": "#CFCFCF",
            "ambientColor": "#050506",
            "minContrast": 4.5,
        },
        "defaults": {"scrim": 0.65, "saturation": 1.0},
        "minScrim": 0.20,
        "frozen": False,
    },
}

# The profile whose scrim is mirrored to the top-level `overlayAlpha` key, for clients that
# predate `render` blocks entirely. Frozen: app 1.2 reads this and nothing else.
LEGACY_PROFILE = "scrim-lerp-1"

AMBIENT_RGB = (5, 5, 6)

# Rendered chroma a scene should reach before the measurement stops helping it, and the ceiling on
# that help. Most scenes measure above the floor and are left at 1.0 - a blanket multiplier wrecks
# scenes that are already saturated. Mirrors MAX_SCENE_SATURATION in SceneGrade.kt.
CHROMA_FLOOR = 0.26
MAX_SATURATION = 1.5
BLUR_PX_AT_3X = 7.5  # SCENE_BLUR_RADIUS (2.5.dp) at 3x density
PHONE_W, PHONE_H = 1080, 2340

MIN_CONTRAST = 4.5      # WCAG AA for body text
MAX_OVERLAY_ALPHA = 0.88  # past this the scene is more overlay than art; warn instead

# The scrim exists to guarantee text contrast, not to darken for its own sake, so the search
# starts low and only climbs if the text needs it. The multiply reaches MIN_CONTRAST well below
# where the old lerp did, which is why this floor is lower than it looks.
MIN_OVERLAY_ALPHA = 0.20

# Below this the art is too dark to read as a place and showing a background stops being worth
# it. Measured on the *rendered* result - blurred, with this scene's own overlay applied - because
# that is what the reader sees. An earlier version measured the source instead and was wrong about
# which scenes were in trouble: a 0.05 source that earns a 0.45 overlay renders brighter than a
# 0.09 source pushed to 0.72, so the source alone cannot tell you. For reference the rendered
# median across the catalog sits near 0.038.
MIN_FINAL_LUMINANCE = 0.020


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


def _blurred_for_measurement(im: Image.Image, blur_dp: float = 2.5) -> Image.Image:
    """Simulate the reader's view for measurement only — never saved.

    Centre-cropping to a phone here is a worst-case probe, not a framing decision: the phone
    aspect keeps the least of the frame, so a scene that passes here passes on wider screens too.
    """
    scale = max(PHONE_W / im.width, PHONE_H / im.height)
    up = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    left, top = (up.width - PHONE_W) // 2, (up.height - PHONE_H) // 2
    crop = up.crop((left, top, left + PHONE_W, top + PHONE_H))
    return crop.filter(ImageFilter.GaussianBlur(blur_dp * 3.0))


def _hex_rgb(value: str):
    v = value.lstrip("#")
    return tuple(int(v[i : i + 2], 16) for i in (0, 2, 4))


def apply_scrim(im: Image.Image, alpha: float, profile: dict) -> Image.Image:
    """The scrim, in whichever maths this profile describes.

    `multiply` scales every channel toward a near-black floor, which holds a scene's own colour
    relationships. `lerp` blends toward a near-neutral, which pulls them to grey - correct only
    because that is what the client reading those numbers actually does.
    """
    if profile["mode"] == "multiply":
        floor = _hex_rgb(profile["calibration"]["ambientColor"])
        return Image.merge("RGB", tuple(
            im.getchannel(ch).point(lambda c, i=i: round(c * (1 - alpha) + floor[i] * alpha))
            for i, ch in enumerate("RGB")))
    overlay = _hex_rgb(profile["calibration"]["overlayColor"])
    return Image.blend(im, Image.new("RGB", im.size, overlay), alpha)


def seed_keywords(name: str, description: str, lexicon: set) -> list:
    """Place vocabulary for one scene: its name, plus place nouns its description already uses.

    Seeded rather than authored, so every scene has something from day one and a human can add
    the synonyms a reader's page might actually use - "trolley", "checkout", "groceries" for a
    supermarket - which no automatic pass will find.
    """
    stop = {
        "the", "and", "for", "with", "from", "into", "over", "under", "small", "large", "big",
        "late", "early", "night", "day", "morning", "afternoon", "evening", "midnight", "dawn",
        "dusk", "after", "hours", "above", "below", "empty", "covered", "quiet", "old", "new",
    }
    words = [w for w in re.split(r"[^a-z]+", name.lower()) if len(w) > 3 and w not in stop]
    body = {w for w in re.split(r"[^a-z]+", description.lower()) if w in lexicon}
    return sorted(set(words) | body)


def read_hand_lexicon() -> set:
    """The app's hand-written place nouns, so seeding can reuse them rather than duplicate them."""
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "app", "src", "main", "java",
        "com", "immersialabs", "infinitereading", "domain", "environment", "PlaceLexicon.kt",
    )
    if not os.path.isfile(path):
        return set()
    src = open(path).read()
    # Only the WORDS set. The file also holds NAME_STOP - "the", "and", "late", "night" - and
    # reading the whole file swept those in, so every scene was seeded with function words.
    block = re.search(r"val WORDS\s*=\s*setOf\((.*?)\n\s*\)", src, re.S)
    return set(re.findall(r'"([a-z][a-z -]+)"', block.group(1))) if block else set()


def mean_chroma(im: Image.Image) -> float:
    """How much colour survives, 0 = neutral grey. Sampled coarsely, like the other measures."""
    px = list(im.resize((48, 104)).getdata())
    return sum((max(p) - min(p)) / max(1, max(p)) for p in px) / len(px)


def saturate(im: Image.Image, amount: float) -> Image.Image:
    """Matches the saturation step in SceneGrade.kt: mix between luma and the original."""
    return ImageEnhance.Color(im).enhance(amount)


def required_saturation(blurred: Image.Image) -> float:
    """Lift for a scene that blurs out grey. 1.0 for anything already at CHROMA_FLOOR."""
    c = mean_chroma(blurred)
    if c <= 0.001:
        return MAX_SATURATION
    return round(min(MAX_SATURATION, max(1.0, CHROMA_FLOOR / c)), 2)


def worst_region_contrast(graded: Image.Image, text_rgb) -> float:
    """Contrast against the brightest 5% of the frame, where light text suffers most."""
    tiles = list(graded.resize((24, 52)).getdata())
    tiles.sort(key=luminance, reverse=True)
    worst = tiles[: max(1, len(tiles) // 20)]
    avg = tuple(sum(t[i] for t in worst) // len(worst) for i in range(3))
    return contrast(text_rgb, avg)


def required_scrim(blurred: Image.Image, profile: dict):
    """Minimum scrim keeping text at this profile's minContrast. Returns (scrim, achieved)."""
    text_rgb = _hex_rgb(profile["calibration"]["textColor"])
    floor = profile["minScrim"]
    target = profile["calibration"]["minContrast"]
    alpha = floor
    achieved = worst_region_contrast(apply_scrim(blurred, alpha, profile), text_rgb)
    while achieved < target and alpha < MAX_OVERLAY_ALPHA:
        alpha = round(alpha + 0.01, 2)
        achieved = worst_region_contrast(apply_scrim(blurred, alpha, profile), text_rgb)
    return alpha, achieved


def measure_profile(im: Image.Image, profile: dict, published: dict | None = None) -> dict:
    """Everything one profile needs for one scene, measured at that profile's own blur.

    For a frozen profile an already-published scrim is kept whenever it still clears the contract,
    rather than replaced by a freshly measured one that differs by a rounding step. Clients in the
    field are reading the published number; re-deriving it every run would hand them churn for no
    legibility gain.
    """
    blurred = _blurred_for_measurement(im, profile["calibration"]["blurDp"])
    block = {}
    graded = blurred
    if profile["saturation"]:
        sat = required_saturation(blurred)
        if sat != 1.0:
            block["saturation"] = sat
            graded = saturate(blurred, sat)

    text_rgb = _hex_rgb(profile["calibration"]["textColor"])
    target = profile["calibration"]["minContrast"]
    kept = None
    if profile.get("frozen") and published and "scrim" in published:
        candidate = published["scrim"]
        if worst_region_contrast(apply_scrim(graded, candidate, profile), text_rgb) >= target:
            kept = candidate

    if kept is not None:
        scrim = kept
        achieved = worst_region_contrast(apply_scrim(graded, scrim, profile), text_rgb)
        block["_kept"] = True
    else:
        scrim, achieved = required_scrim(graded, profile)
    block["scrim"] = scrim
    block["_achieved"] = achieved
    block["_rendered"] = rendered_luminance(apply_scrim(graded, scrim, profile))
    return block


def check_calibration_immutable(manifest: dict):
    """A published profile's calibration may never change - its scene numbers assume it.

    This is the guard that the lerp -> multiply migration needed and did not have. Recalibrating
    in place silently invalidates every number already in the hands of released clients; the only
    safe move is a new profile id.
    """
    published = manifest.get("profiles", {})
    for pid, live in published.items():
        if pid not in PROFILES:
            continue                       # a profile this script no longer measures; left alone
        old, new = live.get("calibration"), PROFILES[pid]["calibration"]
        if old and old != new:
            changed = {k: (old.get(k), new.get(k)) for k in set(old) | set(new)
                       if old.get(k) != new.get(k)}
            raise SystemExit(
                f"error: calibration for published profile '{pid}' would change: {changed}.\n"
                f"       Scene numbers already published under that id assume the old values, and\n"
                f"       clients in the field cannot be told otherwise. Add a NEW profile id\n"
                f"       instead, and leave '{pid}' exactly as it is."
            )


def scene_luminance(im: Image.Image) -> float:
    """Mean relative luminance of the blurred scene, before any overlay.

    This is the ceiling on how visible the art can ever be: the overlay only subtracts.
    """
    px = list(_blurred_for_measurement(im).resize((48, 104)).getdata())
    return sum(luminance(p) for p in px) / len(px)


def rendered_luminance(graded: Image.Image) -> float:
    """Mean luminance of the scene exactly as the reader sees it."""
    px = list(graded.resize((48, 104)).getdata())
    return sum(luminance(p) for p in px) / len(px)


SCENE_KEY_ORDER = (
    "id", "name", "world", "kind", "description", "imageUrl", "overlayAlpha", "render",
    "keywords", "cues", "examples",
)


def in_published_order(scene: dict) -> dict:
    ordered = {k: scene[k] for k in SCENE_KEY_ORDER if k in scene}
    ordered.update((k, v) for k, v in scene.items() if k not in ordered)
    return ordered


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    measure_only = "--measure-only" in sys.argv[1:]
    here = os.path.dirname(os.path.abspath(__file__))
    if args:
        input_dir = args[0]
    elif measure_only:
        input_dir = os.path.join(here, "scenes")
    else:
        print("usage: prepare-images.py <input-dir> | --measure-only [<dir>]", file=sys.stderr)
        return 64
    manifest_path = os.path.join(here, "manifest.json")
    out_dir = os.path.join(here, "scenes")

    if not os.path.isdir(input_dir):
        print(f"error: no such directory: {input_dir}", file=sys.stderr)
        return 66
    if not os.path.isfile(manifest_path):
        print(f"error: manifest not found: {manifest_path}", file=sys.stderr)
        return 66
    if not measure_only:
        os.makedirs(out_dir, exist_ok=True)

    sources = sorted(
        f for f in os.listdir(input_dir)
        if os.path.splitext(f)[1].lower() in (".jpg", ".jpeg", ".png", ".webp")
    )
    if not sources:
        print(f"error: no images found in {input_dir}", file=sys.stderr)
        return 66

    print(f"  {'scene':<26}{'in':>8}{'out':>7}  {'grade':<20}{'dim':<12}{'contrast':>9}")
    print(f"  {'-' * 76}")

    warnings = []
    render = {}

    # What is already published, so a frozen profile can be preserved rather than re-derived.
    # Falls back to the pre-profiles top-level key for a manifest written before schema 2.
    prior_manifest = json.load(open(manifest_path))
    check_calibration_immutable(prior_manifest)
    published_blocks = {}
    for scene in prior_manifest.get("scenes", []):
        blocks = dict(scene.get("render", {}))
        if LEGACY_PROFILE not in blocks and "overlayAlpha" in scene:
            blocks[LEGACY_PROFILE] = {"scrim": scene["overlayAlpha"]}
        published_blocks[scene["id"]] = blocks
    for name in sources:
        scene_id = os.path.splitext(name)[0]
        src_path = os.path.join(input_dir, name)
        im = Image.open(src_path).convert("RGB")

        if im.width > im.height:
            warnings.append(
                f"{scene_id}: landscape ({im.width}x{im.height}); scenes are centre-cropped on a "
                f"portrait screen so the sides will be lost. Portrait 2:3 is preferred."
            )

        # Downscale only. A master smaller than SHORT_EDGE carries no extra detail to recover, so
        # enlarging it would just spend bytes on interpolation - and these are blurred at runtime,
        # where the difference is invisible anyway.
        scale = 1.0 if measure_only else min(1.0, SHORT_EDGE / min(im.width, im.height))
        if scale < 1.0:
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        elif min(im.width, im.height) < SHORT_EDGE and not measure_only:
            # Not worth saying in --measure-only: the input there is already-published art, and
            # every scene would repeat it.
            warnings.append(
                f"{scene_id}: master is {im.width}x{im.height}, short edge under {SHORT_EDGE}px; "
                f"kept at native size rather than upscaled."
            )

        # Every profile, every run. Measuring them together is the whole point: a projection
        # cannot go stale if it is never written alone.
        prior = published_blocks.get(scene_id, {})
        blocks = {
            pid: measure_profile(im, prof, prior.get(pid))
            for pid, prof in PROFILES.items()
        }
        render[scene_id] = blocks

        active = blocks[LEGACY_PROFILE]
        for pid, block in blocks.items():
            prof = PROFILES[pid]
            if block["_achieved"] < prof["calibration"]["minContrast"]:
                warnings.append(
                    f"{scene_id}: {pid} only reaches {block['_achieved']:.1f}:1 at scrim "
                    f"{block['scrim']:.2f} — the source is too bright. Regenerate it darker or "
                    f"with less open sky."
                )
            if block["_rendered"] < MIN_FINAL_LUMINANCE:
                warnings.append(
                    f"{scene_id}: {pid} renders at {block['_rendered']:.3f}, below "
                    f"{MIN_FINAL_LUMINANCE:.3f} — too dark to read as a place. Regenerate with "
                    f"light spread over larger areas (wet surfaces, sky glow, lit facades), not "
                    f"more small bright points."
                )
        note = " ".join(
            f"{pid.split('-')[1]}:{b['scrim']:.2f}"
            + (f"/{b['saturation']:.2f}" if "saturation" in b else "")
            for pid, b in blocks.items()
        )
        achieved = min(b["_achieved"] for b in blocks.values())
        if any(b.get("_kept") for b in blocks.values()):
            note += "  (frozen kept)"

        out_path = os.path.join(out_dir, f"{scene_id}.webp")
        if not measure_only:
            im.save(out_path, "WEBP", quality=QUALITY, method=6)

        print(
            f"  {scene_id:<26}"
            f"{os.path.getsize(src_path)//1024:>7}K"
            f"{os.path.getsize(out_path)//1024:>6}K"
            f"  {note:<34}"
            f"{f'{im.width}x{im.height}':<12}"
            f"{achieved:>7.1f}:1"
        )

    for w in warnings:
        print(f"\n  warning: {w}", file=sys.stderr)

    # Write the measured overlay back into the manifest so the app applies it at runtime and the
    # art stays untouched.
    manifest = prior_manifest
    hand_lexicon = read_hand_lexicon()

    manifest["schema"] = SCHEMA_VERSION
    manifest["profiles"] = {
        pid: {
            "summary": prof["summary"],
            "calibration": prof["calibration"],
            "defaults": prof["defaults"],
        }
        for pid, prof in PROFILES.items()
    }
    for scene in manifest["scenes"]:
        # Only touch scenes this run actually measured. Re-running on a folder of one new scene
        # must not strip the overlay from every scene that was not in it.
        if scene["id"] not in render:
            continue
        blocks = render[scene["id"]]
        # Authored content is never touched by a re-measure. `examples` and `cues` have no
        # seeding at all - prose in the register of a novel is not something to generate from a
        # description, and a cue is a judgement about what a page would say rather than about what
        # is in the picture. `keywords` is seeded once and then left alone; delete the key to have
        # it regenerated from the name and description.
        if not scene.get("keywords"):
            scene["keywords"] = seed_keywords(
                scene.get("name", ""), scene.get("description", ""), hand_lexicon
            )
        scene["render"] = {
            pid: {k: v for k, v in block.items() if not k.startswith("_")}
            for pid, block in blocks.items()
        }
        # Frozen mirror for clients that predate `render` blocks entirely (app 1.2 reads this and
        # nothing else). Written from the same measurement, so it cannot drift from its profile.
        scene["overlayAlpha"] = blocks[LEGACY_PROFILE]["scrim"]
        # `saturation` was briefly published at the top level before profiles existed. It only
        # ever meant the multiply profile's value, and no released client reads it, so it goes.
        scene.pop("saturation", None)
    # A scene merged from staged/ arrives without overlayAlpha or render, so both would land at the
    # end of the entry. Put every measured scene's keys in the published order; the scenes already
    # published are in it, so they do not move.
    manifest["scenes"] = [
        in_published_order(scene) if scene["id"] in render else scene
        for scene in manifest["scenes"]
    ]
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
