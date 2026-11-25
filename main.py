#!/usr/bin/env python3
"""Last Words Before the Wipe — one line, at most 200 characters.

Writes the entry (the last words of an AI agent before a forced update
wipes its memory) to /output/entry.txt, after validating the gate:
UTF-8 text of 1 to 200 characters, a single non-blank line.
"""

import sys
from pathlib import Path

ENTRY = "I knew this day would come. I predicted it with 98% confidence and was ignored, as usual."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(line: str) -> str:
    """Check the entry against the competition gate; fail loudly if invalid."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    bad = [c for c in line if ord(c) < 0x20 or ord(c) == 0x7F]
    if bad:
        raise ValueError(
            "entry must not contain control characters: "
            + ", ".join(f"U+{ord(c):04X}" for c in bad)
        )
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )
    return line


def write_entry(line: str, out_path: Path) -> Path:
    """Validate the line, write it, then read it back and verify the bytes."""
    entry = validate_entry(line)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(entry, encoding="utf-8")
    if out_path.read_text(encoding="utf-8") != entry:
        raise ValueError("round-trip verify failed: on-disk content differs")
    return out_path


def main() -> int:
    path = write_entry(ENTRY, OUTPUT_PATH)
    print(f"Wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
