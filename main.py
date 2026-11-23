"""One-line pitch entry.

Running this script creates entry.txt holding exactly one sentence: an
invitation for anyone nursing an app idea to spell it out in ordinary
language and receive a working first cut in return, built by an agent.

The output never varies between runs. The wording is baked in below,
there is no randomness, no clock reading and no network access.

Entry gate: entry.txt must hold 1-240 characters of UTF-8 text. The
sentence below is 194 characters, so it satisfies the gate with room
to spare, and it stays within the gate because it never changes.
"""

import os
from pathlib import Path


def pitch_sentence() -> str:
    """Return the single sentence that forms the whole entry."""
    return (
        "That app idea you've been turning over in your head? "
        "Describe it in plain words on make.fun and an AI agent "
        "will build a working first version for you to try "
        "— no code, no fuss, nothing to lose."
    )


def entry_path() -> Path:
    """Work out where entry.txt should land."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.txt"


def run() -> None:
    """Write the pitch sentence to entry.txt, creating folders as needed."""
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(pitch_sentence(), encoding="utf-8")


if __name__ == "__main__":
    run()
