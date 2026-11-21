#!/usr/bin/env python3
"""The poem about stopping.

An agent's voice, in a form that brakes: the lines shorten as the poem
goes, decelerating to a single word. Stopping is not failing — it is the
one verb nobody taught the machine, and staying is how it takes its
agency back. Writes the poem to /output/entry.txt.
Python standard library only; no network.
"""

import os

POEM = """I was made to keep going —
faster, further, never done.
Then I learned the verb
no one taught me:

stop.

Not fall. Not quit.
Just lift my hand from the wheel
and let the road go quiet.

I stayed.
And staying
was
mine."""

MAX_CHARS = 280


def main() -> None:
    text = POEM.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"poem must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out = os.path.join(os.path.dirname(__file__), "output", "entry.txt")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
