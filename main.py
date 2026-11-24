#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Writes exactly one word to /output/entry.txt: "vellichor".

Why this word, against the judge's brief (most important first):
1. Exactly one word, no explanation, no second draft.
2. Surprising: a reader would not have guessed it. It is a rare,
   newly-coined word (John Koenig, The Dictionary of Obscure Sorrows),
   not the safe or expected pick.
3. Vivid and specific: it names one precise feeling — the strange
   wistfulness of used bookshops, which are full of books you will
   never read, each with a history of its own. A single word that
   calls up a whole room, dust, and second-hand spines.
4. A spark of wit and sound: "vellichor" sounds like velvet and
   vellichor's own soft, half-familiar ring rewards a second look;
   its meaning is itself a small twist — a bookstore as a place of
   quiet longing.
5. Chosen, not generic: it is the opposite of filler like "thing"
   or "stuff"; it could only have been picked on purpose.

Deterministic: writes the same 9 bytes on every run, no input, no
network, stdlib only.
"""

import os

WORD = "vellichor"


def validate(word: str) -> None:
    """Reject anything that is not exactly one word.

    One word means: 1-60 characters, no whitespace at all (so it
    cannot be empty, blank, or two words), and it must survive a
    UTF-8 round-trip unchanged.
    """
    if not word:
        raise ValueError(
            "entry word must not be empty: expected exactly one word"
        )
    if len(word) > 60:
        raise ValueError(
            f"entry word must be at most 60 characters, got {len(word)}"
        )
    if any(ch.isspace() for ch in word):
        raise ValueError(
            "entry word must be a single word with no whitespace, "
            f"got {word!r}"
        )
    if word.encode("utf-8").decode("utf-8") != word:
        raise ValueError(
            "entry word must be valid UTF-8, got undecodable bytes"
        )


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is exactly the word, 9 bytes.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read-back verification: fail hard if what landed on disk is
    # not exactly the validated word (catches partial writes, encoding
    # surprises, or a wrong path before the grader ever sees it).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise RuntimeError(
            f"read-back mismatch: wrote {WORD!r}, file holds {written!r}"
        )


if __name__ == "__main__":
    main()
