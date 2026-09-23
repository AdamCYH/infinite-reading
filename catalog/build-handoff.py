#!/usr/bin/env python3
"""Build the file an image agent is given: the brief, then one prompt per scene.

    ./build-handoff.py                    # HANDOFF.md: every scene published in manifest.json
    ./build-handoff.py --wave 1           # HANDOFF-WAVE-1.md: the scenes staged in staged/wave-1.json
    ./build-handoff.py --only a,b --out HANDOFF-TEST.md

Prompts come from PROMPTS.md and the brief from IMAGE-AGENT-BRIEF.md, so edit those and rebuild
rather than editing a handoff. The agent sees only the id, its [FANTASTIC] or [PERIOD SET] marker
and the prompt: scene names and the history in PROMPTS.md are for us, and would only cost tokens.
Scenes are numbered from 1 in each handoff; the numbers in PROMPTS.md mean nothing to the agent.
"""

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEADING = re.compile(r"^#### \d+\. `([a-z0-9-]+)`(?: — [^*]*?)?(?:\s+\*\*\[([A-Z ]+)\]\*\*)?\s*$")
MARKERS = {"FANTASTIC", "PERIOD SET"}


def read_prompts():
    """Every prompt in PROMPTS.md, in file order: id -> (marker or None, prompt on one line)."""
    prompts = {}
    lines = (HERE / "PROMPTS.md").read_text().splitlines()
    i = 0
    while i < len(lines):
        m = HEADING.match(lines[i])
        i += 1
        if not m:
            continue
        scene_id, marker = m.group(1), m.group(2)
        if marker is not None and marker not in MARKERS:
            sys.exit(f"{scene_id}: unknown marker [{marker}]")
        if scene_id in prompts:
            sys.exit(f"{scene_id}: two prompts in PROMPTS.md")
        while i < len(lines) and not lines[i].strip():
            i += 1
        quoted = []
        while i < len(lines) and lines[i].startswith(">"):
            quoted.append(lines[i][1:].strip())
            i += 1
        if not quoted:
            sys.exit(f"{scene_id}: heading with no quoted prompt under it")
        prompts[scene_id] = (marker, " ".join(quoted))
    return prompts


def ids_in(path):
    data = json.loads(path.read_text())
    scenes = data["scenes"] if isinstance(data, dict) else data
    return [scene["id"] for scene in scenes]


def build(ids, prompts):
    missing = [scene_id for scene_id in ids if scene_id not in prompts]
    if missing:
        sys.exit("no prompt in PROMPTS.md for: " + ", ".join(missing))
    if len(set(ids)) != len(ids):
        sys.exit("an id is listed twice")
    brief = (HERE / "IMAGE-AGENT-BRIEF.md").read_text().rstrip("\n")
    parts = [brief, "", "---", "", f"# The {len(ids)} scenes", ""]
    for n, scene_id in enumerate(ids, start=1):
        marker, prompt = prompts[scene_id]
        tag = f"  **[{marker}]**" if marker else ""
        parts += [f"### {n}. `{scene_id}`{tag}", "", f"> {prompt}", ""]
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--wave", type=int, help="take the scenes staged in staged/wave-N.json")
    parser.add_argument("--only", help="comma-separated ids, in the order to hand them over")
    parser.add_argument("--out", help="file to write, relative to this folder")
    args = parser.parse_args()

    prompts = read_prompts()
    if args.wave is not None:
        ids = ids_in(HERE / "staged" / f"wave-{args.wave}.json")
        default_out = f"HANDOFF-WAVE-{args.wave}.md"
    else:
        ids = ids_in(HERE / "manifest.json")
        default_out = "HANDOFF.md"
    if args.only:
        chosen = [scene_id.strip() for scene_id in args.only.split(",") if scene_id.strip()]
        outside = [scene_id for scene_id in chosen if scene_id not in ids]
        if outside:
            sys.exit("not in the chosen set: " + ", ".join(outside))
        ids = chosen
        if not args.out:
            sys.exit("--only needs --out, so a partial list never overwrites a full handoff")
    out = HERE / (args.out or default_out)
    out.write_text(build(ids, prompts))
    print(f"{out.name}: {len(ids)} scenes")


if __name__ == "__main__":
    main()
