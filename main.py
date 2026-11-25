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


def validate_entry(entry: str) -> None:
    """Guard the one-line entry before it is written.

    The bounty scores a single short line; a stray newline, an overlong
    line, or a multi-sentence ramble would break the format and sink
    the entry, so the script refuses to write anything that does not
    satisfy the winners' recipe constraints instead of silently
    producing a malformed file.
    """
    assert isinstance(entry, str) and entry, "entry must be a non-empty string"
    assert 1 <= len(entry) <= 140, f"entry must be 1-140 chars, got {len(entry)}"
    assert len(entry.split()) <= 20, f"entry must be <= 20 words, got {len(entry.split())}"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert entry == entry.strip(), "entry must not have leading/trailing whitespace"
    assert not entry.endswith("\n"), "entry must not end with a trailing newline"


def main() -> None:
    validate_entry(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
