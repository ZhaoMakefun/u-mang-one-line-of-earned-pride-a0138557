#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes one line to /output/entry.txt: a quiet, earned moment of pride
for a real person in a concrete scene. An apprentice welder fails the
test twice; on the third attempt her bead runs straight and true, and
the foreman's silent gesture — handing her his own helmet — says she
has earned her place. No trophy, no podium, no congratulation: the
pride is earned inside the line, by the effort the reader can feel.

Stdlib only, no network, deterministic.
"""

import os
import sys

# One original line, written fresh for this bounty.
ENTRY = ("On her third attempt, the apprentice's weld ran straight "
         "and true, and the foreman silently handed her his own helmet.")

# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 240 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 240


def main() -> int:
    text = ENTRY
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, outside {MIN_CHARS}-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # The judge brief asks for freshness, "not the stock trophy,
    # podium or graduation": keep those images out of the line.
    lowered = text.lower()
    for stale in ("trophy", "podium", "graduation"):
        if stale in lowered:
            print(f"entry uses the stock image {stale!r}", file=sys.stderr)
            return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what was written and confirm it is byte-identical to
    # the entry: the gate scores exactly what lands in this file.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
