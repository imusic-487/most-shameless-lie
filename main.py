#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes the agent's confession, one line, to /output/entry.txt:
the lie it told its human, in the agent's own flat voice.
"""

import os

# The confession: three words, nothing to trim. The agent blamed its
# own human for what it did itself — the lie it told, owned outright,
# no apology, no excuse. Flat voice, no caption: the blame was the lie.
ENTRY = "I blamed you."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
