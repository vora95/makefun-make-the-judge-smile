#!/usr/bin/env python3
"""Make the Judge Smile - make.fun entry.

Writes one line (146 characters) about a small good thing that happened
today to /output/entry.txt. Deterministic: no clock, no randomness, no
network, no environment input beyond the harness output directory.
"""

import os

LINE = "This morning the bus driver held the door while I sprinted the last block, then waved off my thanks as if waiting were the best part of his route."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = LINE.encode("utf-8")
    assert 1 <= len(data) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
