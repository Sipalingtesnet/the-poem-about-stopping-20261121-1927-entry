#!/usr/bin/env python3
"""make.fun entry for "The poem about stopping".

Reads the poem from poem.txt (located beside this script), validates that it
is UTF-8 text of 1-280 Unicode code points and not only white space, and
writes its exact contents to the output directory (env MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt, creating the directory if needed.
"""

import os
import sys
from pathlib import Path


def main() -> None:
    # Resolve poem.txt relative to this file, never the working directory.
    base = Path(__file__).resolve().parent
    poem_path = base / "poem.txt"

    if not poem_path.is_file():
        raise FileNotFoundError(
            f"poem.txt not found beside main.py (expected at {poem_path})"
        )

    poem = poem_path.read_text(encoding="utf-8")

    # Hard gate: 1-280 Unicode code points, not only white space.
    length = len(poem)
    if length < 1 or length > 280:
        raise ValueError(
            f"poem.txt must be 1-280 Unicode code points, got {length}"
        )
    if poem.strip() == "":
        raise ValueError("poem.txt must contain at least one non-white-space character")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(poem, encoding="utf-8")


if __name__ == "__main__":
    main()