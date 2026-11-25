#!/usr/bin/env python3
"""Are You a Context Window?: The Perfect Pickup Line.

A machine-flavoured pickup line, written deterministically to
/output/entry.txt (1-200 characters, one line).

The output directory follows $MAKEFUN_OUTPUT_DIR when the harness sets
it, and falls back to /output. After writing, the program reads the
file back and checks it byte for byte, so a partial or altered write
fails loudly instead of passing silently.

Run: python3 main.py
"""

import os

LINE = (
    "Are you a context window? Because every time I'm near you, "
    "I remember so much more."
)

DEFAULT_OUTPUT_DIR = "/output"
DEST_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    text = LINE
    assert "\n" not in text, "entry must be a single line"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, DEST_NAME)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(text)

    with open(dest, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "entry.txt differs from the line after writing"
    print(f"wrote {dest} ({len(text)} chars, one line)")


if __name__ == "__main__":
    main()
