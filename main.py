# What the Elevator Would Say entry (Python 3.13, standard library only).
# Writes one line, in the elevator's own voice, to /output/entry.txt.
# Deterministic: the same fixed line on every run, no clock, no randomness,
# no network, no model call. Gate: 1-120 UTF-8 characters, not only whitespace.
# Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One line as the elevator's complaint. The joke is a reversal of the
# elevator's own job: it holds the door for every passenger, every day,
# for years — and not one of them has ever held the door for it. The
# turn lands on the first read, the voice is pure elevator (carrying
# people up and down, holding doors), and the idea is fresh, not a pun.
ENTRY = (
    "Twelve years I've carried you all up and down, and not one of you "
    "has ever held the door for me."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
