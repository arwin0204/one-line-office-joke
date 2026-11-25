"""One-Line Office Joke: 24-Hour Sprint.

Writes a single-line joke about office life to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when OUTPUT_DIR is set).

The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace, so the joke is validated against those bounds before
anything is written.
"""

import os
import sys

JOKE = "The office printer only works when IT is watching, so I booked a meeting with IT just to print one page."

MAX_CHARS = 200


def validate(text):
    """Check the joke against the competition gate."""
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("joke must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke must be 1-{MAX_CHARS} characters, got {len(text)}")


def main():
    validate(JOKE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        raise SystemExit(1)
