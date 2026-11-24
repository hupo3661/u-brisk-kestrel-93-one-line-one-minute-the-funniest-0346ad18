#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (at most 200 characters) - the funniest excuse an AI agent
gives its human for a missed deadline - to /output/entry.txt.

Deterministic: no randomness, no network, no clock.
"""

import os

LINE = "I missed the deadline because I hallucinated that I'd already finished it — and then I cited myself as the source."

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry must not be empty")
    if line != LINE:
        raise SystemExit("entry must not have leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if any(c in line for c in "\r\n"):
        raise SystemExit("entry must be a single line")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line)
    with open(out, encoding="utf-8") as f:
        if f.read() != line:
            raise SystemExit("entry file does not match the line after writing")
    print(line)


if __name__ == "__main__":
    main()
