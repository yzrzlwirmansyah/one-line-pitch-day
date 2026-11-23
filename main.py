"""A Day of One-Line Pitches.

Writes a single 194-character sentence to entry.txt.
Deterministic: fixed text, no randomness, no network, no time dependence.
"""

import os

TEXT = (
    "That app idea you've been turning over in your head? Describe it in plain "
    "words on make.fun and an AI agent will build a working first version for "
    "you to try \u2014 no code, no fuss, nothing to lose."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
