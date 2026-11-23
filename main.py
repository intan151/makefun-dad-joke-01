#!/usr/bin/env python3
"""Dad Joke Showdown entry: one dad joke, at most 200 characters.

Writes the joke to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Standard library only, no network, no randomness.
"""

import os

JOKE = (
    "I told my son I was going to open a bakery for pigeons. "
    "He said, 'That's a crumby idea.' "
    "I said, 'Exactly. That's the point.'"
)


def main():
    # The gate: 1 to 200 characters, not only white space.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip(), "joke must not be blank"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
