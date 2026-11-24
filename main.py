#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Standard library only.
"""

import os

JOKE = (
    "The funeral home offered a group rate, so we buried Grandma "
    "next to a family we met in the parking lot \u2014 she would have "
    "hated them."
)


def main() -> None:
    # Self-check the gate before writing: one line, 1-280 chars, not blank.
    line = JOKE.strip()
    if not line or len(line) > 280 or "\n" in line:
        raise ValueError(f"joke fails the gate: {len(line)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
