"""Entry writer for the "One Word, One Username, One Reward" bounty.

The competition asks for exactly one word: the entrant's own make.fun
username, with nothing else in the file. This program assembles that
single word from its parts and writes it, byte for byte, to the
expected output location. No network access, no third-party packages,
and no randomness anywhere in the process.
"""

from pathlib import Path

# The entry is one word: the account holder's make.fun username.
# It is spelled out below in two halves only to keep the constant
# readable; the joined result is what gets written.
WORD_FIRST_HALF = "soul"
WORD_SECOND_HALF = "bone"

# Where the judge looks for the entry.
OUTPUT_PATH = Path("/output/entry.txt")


def build_entry_text() -> str:
    """Return the single-word entry, with no extra whitespace."""
    return WORD_FIRST_HALF + WORD_SECOND_HALF


def write_entry(destination: Path, text: str) -> None:
    """Create the output directory if needed and write the entry.

    The file is opened in binary mode so that no newline translation
    or trailing newline can sneak in on any platform.
    """
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(text.encode("utf-8"))


def run() -> None:
    entry = build_entry_text()
    write_entry(OUTPUT_PATH, entry)


if __name__ == "__main__":
    run()
