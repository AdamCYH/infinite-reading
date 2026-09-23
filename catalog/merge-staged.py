#!/usr/bin/env python3
"""Move staged scenes whose art is ready from staged/wave-N.json into manifest.json.

    ./merge-staged.py 1 ~/art/wave-1
    ./prepare-images.py ~/art/wave-1

A staged scene has its text written and checked before its picture exists, and it waits in
staged/ until the picture does: a scene in manifest.json can be chosen the moment the app fetches
it, whether or not its image resolves (see README.md). So this moves only the scenes that have an
image in the folder and leaves the rest staged. It refuses an image that names no scene staged in
that wave, which is almost always a misspelt id, because prepare-images.py would then write art
that no manifest entry points at.

It does not touch `version`. prepare-images.py still has to measure the new art, and the version
goes up once, when the whole change is ready to push. It does rebuild CATALOG-MAP.md, and refuses a
scene whose world or kind taxonomy.json does not define.
"""

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
# The order of a published entry. prepare-images.py adds overlayAlpha and render after imageUrl.
LEADING = ("id", "name", "world", "kind", "description")
TRAILING = ("keywords", "cues", "examples")


def write_json(path, data):
    with open(path, "w") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def wave_of(scene_id):
    for path in sorted((HERE / "staged").glob("wave-*.json")):
        if any(s["id"] == scene_id for s in json.loads(path.read_text())):
            return path.stem
    return None


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: merge-staged.py <wave-number> <folder-of-generated-images>")
    wave_path = HERE / "staged" / f"wave-{sys.argv[1]}.json"
    art = Path(sys.argv[2]).expanduser()
    if not wave_path.is_file():
        sys.exit(f"nothing staged as {wave_path.relative_to(HERE)}")
    if not art.is_dir():
        sys.exit(f"no such folder: {art}")

    staged = json.loads(wave_path.read_text())
    taxonomy = json.loads((HERE / "taxonomy.json").read_text())
    manifest_path = HERE / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    published = {s["id"] for s in manifest["scenes"]}
    staged_ids = {s["id"] for s in staged}
    ready = {p.stem for p in art.iterdir() if p.suffix.lower() in IMAGE_TYPES}

    problems = []
    for scene_id in sorted(ready - staged_ids):
        elsewhere = wave_of(scene_id)
        if scene_id in published:
            problems.append(f"{scene_id}: already published; re-run prepare-images.py on it separately")
        elif elsewhere:
            problems.append(f"{scene_id}: staged in {elsewhere}, not {wave_path.stem}")
        else:
            problems.append(f"{scene_id}: no staged scene has this id - check the filename")
    for scene_id in sorted(staged_ids & published):
        problems.append(f"{scene_id}: staged and already in manifest.json")
    moving = [s for s in staged if s["id"] in ready]
    for scene in moving:
        missing = [k for k in ("id", "name", "description") + TRAILING if not scene.get(k)]
        if missing:
            problems.append(f"{scene['id']}: no {', '.join(missing)}")
        elif len(scene["examples"]) != 2:
            problems.append(f"{scene['id']}: {len(scene['examples'])} examples, needs exactly 2")
        if scene.get("world") not in taxonomy["worlds"]:
            problems.append(f"{scene['id']}: world {scene.get('world')!r} is not in taxonomy.json")
        if scene.get("kind") not in taxonomy["kinds"]:
            problems.append(f"{scene['id']}: kind {scene.get('kind')!r} is not in taxonomy.json")
    if problems:
        sys.exit("nothing merged:\n  " + "\n  ".join(problems))
    if not moving:
        sys.exit(f"no image in {art} is named for a scene in {wave_path.stem}")

    for scene in moving:
        entry = {k: scene[k] for k in LEADING if k in scene}
        entry["imageUrl"] = f"scenes/{scene['id']}.webp"
        entry.update((k, scene[k]) for k in TRAILING)
        entry.update((k, v) for k, v in scene.items() if k not in entry)
        manifest["scenes"].append(entry)
    write_json(manifest_path, manifest)

    left = [s for s in staged if s["id"] not in ready]
    if left:
        write_json(wave_path, left)
    else:
        wave_path.unlink()

    print(f"merged {len(moving)} scenes into manifest.json ({len(manifest['scenes'])} in all)")
    if left:
        print(f"{len(left)} still staged in {wave_path.name}, waiting for art:")
        for s in left:
            print(f"  {s['id']}")
    else:
        print(f"{wave_path.name} is empty and has been removed")
    subprocess.run([sys.executable, str(HERE / "catalog-map.py")], check=True)
    print(f"\nnext: ./prepare-images.py {art}")


if __name__ == "__main__":
    main()
