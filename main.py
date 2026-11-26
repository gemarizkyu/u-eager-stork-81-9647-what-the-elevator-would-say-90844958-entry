"""What the Elevator Would Say — make.fun entry.

Writes the elevator's one complaint, exactly one line, to entry.txt.
Deterministic by construction: no clock, no randomness, no network,
and only the Python standard library is used.
"""

import os
from pathlib import Path

LINE = (
    "Twelve years I've carried you all up and down, "
    "and not one of you has ever held the door for me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = Path(out_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
