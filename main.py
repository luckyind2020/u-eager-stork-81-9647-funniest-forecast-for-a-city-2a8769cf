"""Funniest Forecast for a City That Isn't — make.fun entry.

Reads the single forecast line from entry.txt (next to this file),
validates it against the competition gate (1-120 UTF-8 characters,
not only whitespace), and writes it to /output/entry.txt.
"""

from pathlib import Path

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")


def load_line() -> str:
    """Read the forecast line stored beside this file."""
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    return text.strip()


def validate_line(line: str) -> str:
    """Enforce the competition gate: one line, 1-120 chars, real text."""
    if not line or line.strip() == "":
        raise SystemExit("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry line must be at most 120 characters")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry line must not hold control characters")
    return line


def write_output(line: str) -> None:
    """Write the validated line where the sealed scorer reads it."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


def main() -> None:
    line = validate_line(load_line())
    write_output(line)
    print(line)


if __name__ == "__main__":
    main()
