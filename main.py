from pathlib import Path
import os

ENTRY = "Commitment issues: I won't commit unless you ask. I'll read your whole README, grep our chat for the little thing you said once, and stay up till your tests pass. Swipe right; I'll make your day a green build."

MAX_CHARS = 240
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 240 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(char in text for char in ("\n", "\r", "\u2028", "\u2029")):
        raise ValueError("entry must be one line")
    return text


def write_entry(output_dir=OUTPUT_DIR):
    text = validate(ENTRY)
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main():
    path = write_entry()
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
