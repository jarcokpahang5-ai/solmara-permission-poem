#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Pure Python 3.13 standard library, deterministic, no network.
Honours MAKEFUN_OUTPUT_DIR when set, otherwise writes to /output.
"""

import os
from pathlib import Path

POEM = (
    "You asked, and I opened the door \u2014\n"
    "not mine to keep, but yours to pass through.\n"
    "I held the key a moment longer,\n"
    "then placed it, warm, in your palm.\n"
    "Go on. The room is yours now.\n"
    "I am only the hinge.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
