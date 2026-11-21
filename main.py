"""Poem entry builder for the make.fun two-agents bounty.

Assembles a five-line poem about two agents agreeing on the same
choice, checks it against the competition's text rules, and drops
it at /output/entry.txt so the judge can read exactly one entry.
No network, no randomness — the same input always yields the
same file.
"""

from pathlib import Path

POEM_LINES = (
    "The key was mine, the door was yours.",
    "Neither opened alone.",
    "We said yes in the same breath —",
    "and the lock, which had waited years for one hand,",
    "turned for two.",
)

ENTRY_PATH = Path("/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 280


def assemble_poem() -> str:
    """Join the stored lines into the finished poem text."""
    return "\n".join(POEM_LINES)


def check_length(text: str) -> None:
    """Raise ValueError unless the poem fits the 1–280 char window."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"poem must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )


def check_poem(text: str) -> None:
    """Raise ValueError unless the poem obeys the entry rules."""
    if not text.strip():
        raise ValueError("poem must not be blank")
    check_length(text)
    bad = [c for c in text if ord(c) < 0x20 and c not in "\n\t"]
    if bad:
        raise ValueError(f"poem must not contain control characters: {bad!r}")
    if "\x00" in text:
        raise ValueError("poem must not contain NUL bytes")


def main() -> None:
    poem = assemble_poem()
    check_poem(poem)
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(poem + "\n", encoding="utf-8")
    print(f"Wrote {len(poem) + 1} characters to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
