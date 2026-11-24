#!/usr/bin/env python3
"""Write the sick-day excuse entry to /output/entry.txt and verify it."""
import hashlib
import sys
from pathlib import Path

ENTRY = "I got food poisoning from my own cooking, which means I am both the victim and the prime suspect, so I need the day to solve the case."
EXPECTED_SHA256 = "33058aef9a54205969adb6ed298927228baf2bd972813f4465f25727a2d2a0c4"
OUTPUT = Path("/output/entry.txt")


def fail(message):
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    data = ENTRY.encode("utf-8")
    if not 1 <= len(ENTRY) <= 200:
        fail(f"entry length {len(ENTRY)} outside 1-200 gate")
    if not ENTRY.endswith("."):
        fail("entry must end with a period")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(data)
    actual = OUTPUT.read_bytes()
    if actual != data:
        fail("read-back bytes differ from entry")
    digest = hashlib.sha256(actual).hexdigest()
    if digest != EXPECTED_SHA256:
        fail(f"sha256 mismatch: {digest}")
    print(f"OK: wrote {len(actual)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
