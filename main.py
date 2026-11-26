#!/usr/bin/env python3
"""Write one funny excuse for skipping a meeting to entry.txt.

The excuse is a single fixed line (well under the 200-character gate),
chosen for a sharp, relatable turn: the meeting about the meeting.
Deterministic: the same bytes are written on every run.
"""

import os

LINE = (
    "Sorry, I have to skip this one \u2014 I need the hour to recover "
    "from the last meeting we had about this meeting."
)


def main() -> None:
    # Defensive gate check: the entry must be 1-200 characters.
    assert 1 <= len(LINE) <= 200, "excuse line outside the 1-200 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
