"""A short poem about agency: the power to choose and to act.

The key was mine, the door was yours. Neither opened alone.
We said yes in the same breath -- and the lock, which had waited
years for one hand, turned for two.

The poem is fixed text, written deterministically to
``/output/entry.txt`` with no network access.
"""

from pathlib import Path

POEM = """The key was mine, the door was yours.
Neither opened alone.
We said yes in the same breath —
and the lock, which had waited years for one hand,
turned for two."""

DESTINATION = Path("/output/entry.txt")
POEM_MAX_CHARS = 280


def main() -> int:
    text = POEM + "\n"
    if not 1 <= len(text) <= POEM_MAX_CHARS:
        raise ValueError(f"entry must be 1-{POEM_MAX_CHARS} characters, got {len(text)}")
    if "\x00" in text:
        raise ValueError("entry must not contain NUL bytes")
    if not text.strip():
        raise ValueError("entry must not be blank")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
