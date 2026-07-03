#!/usr/bin/env python3
"""
Build ALL Openline OS badges from badges.json (single source of truth).

Usage:
  python3 build_all.py                 # render every badge into ./out/
  python3 build_all.py --dir os-nav    # render into a specific dir

Re-render everything (e.g. after a style change) by editing gen_badge.py
or badges.json and re-running this script. Slugs are stable, so committing
the new PNGs over the old ones updates every page at once (pages reference
badges by raw GitHub URL + slug).
"""
import json, os, sys, argparse
from gen_badge import build_badge

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.join(HERE, "out"))
    ap.add_argument("--manifest", default=os.path.join(HERE, "badges.json"))
    args = ap.parse_args()
    os.makedirs(args.dir, exist_ok=True)

    with open(args.manifest) as f:
        data = json.load(f)

    # badges list = the 34px pills; assets list = buttons/minis/sec (optional)
    groups = [("badges", data.get("badges", []))]
    if "assets" in data:
        groups.append(("assets", data["assets"]))

    count = 0
    for gname, items in groups:
        for b in items:
            path, size = build_badge(b["label"], b["slug"], b.get("color", "navy"),
                                     b.get("icon", "none"), out_dir=args.dir,
                                     preset=b.get("preset", "badge"))
            print(f"  [{gname:6s}] {b['slug']:30s} {str(size):9s} [{b.get('color')}/{b.get('icon')}/{b.get('preset','badge')}]  {b['label']}")
            count += 1
    print(f"\nDone: {count} images -> {args.dir}")

if __name__ == "__main__":
    main()
