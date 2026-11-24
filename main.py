#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — one line that gets you out of work and gets a laugh.

Writes the entry to /output/entry.txt, reads it back, and verifies the bytes
and the 1-200 character gate. Exits non-zero on any failure.
"""
import os
import sys

LINE = "I got food poisoning from my own cooking, which means I am both the victim and the prime suspect, so I need the day to solve the case."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"gate failed: entry is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        back = f.read()
    if back != LINE:
        print("read-back failed: bytes differ from the entry", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
