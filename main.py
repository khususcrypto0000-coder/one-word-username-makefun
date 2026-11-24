"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username -- one word, nothing else --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Stdlib only. No network, no secrets, no arguments.
"""

import os
import sys

# The entry: Galih's own make.fun username, @khusus-crypto.
# 13 characters: inside the gate's 1-30 character limit, single word.
ENTRY = "khusus-crypto"


def validate(text):
    """Gate check, mirrored from the competition rules: UTF-8 text of
    1-30 characters, not only whitespace, and a single word."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 30:
        raise ValueError("entry must be 1-30 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text.split()) != 1:
        raise ValueError("entry must be a single word")
    return text


def output_dir():
    """Grader output dir: $MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    text = validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Best-effort copy next to this script, so a local run leaves a
    # visible entry.txt beside main.py even without MAKEFUN_OUTPUT_DIR.
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "w",
                  encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError:
        pass

    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
