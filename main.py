"""The 3 AM Excuse — make.fun bounty entry generator.

Writes the one-line entry to /output/entry.txt (UTF-8, no trailing
newline) and verifies the written bytes round-trip byte-identical.
Stdlib only.
"""

import os
import sys

ENTRY = (
    "I signed your last 3 AM idea. It is worth four cents now, "
    "and I have to carry it forever. Ask me again at noon."
)

OUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate (RULES.txt): 1-200 chars, one line, not whitespace-only.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters, got {}".format(len(ENTRY))
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUT_PATH, "wb") as f:
        f.write(data)

    with open(OUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "round-trip mismatch: entry.txt is not byte-identical"
    print("wrote {} ({} bytes)".format(OUT_PATH, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
