#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes the single line a gamer texts the boss to skip work on GTA 6
launch week to /output/entry.txt.

The line is fixed and deterministic: no network, no randomness, no
external input. It is a hurried one-line text built on the winners'
recipe for one-liner/joke categories (one concrete scene, one twist,
no list, no setup, no signature):

  - a specific, boring, almost-believable workplace-adjacent detail
    (overheated console, burnt-plastic smell, waiting on support),
  - the laugh coming from the excuse's own logic: the console died
    doing the one thing he wanted — the GTA 6 preload — so the excuse
    is too honest about GTA 6 to be a lie, and too boring to be a story.
"""

import os

ENTRY = (
    "my ps5 overheated during the preload and now my whole room "
    "smells like burnt plastic, waiting on support"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
