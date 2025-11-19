"""Utility script for copying characters from matching lines.

The script reads a source text file line by line. For every line that contains a
user-provided substring it writes a fixed number of characters from that line to
a destination file. The tool is intended to be used from the command line.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def copy_characters(source: Path, destination: Path, substring: str, char_count: int, *, encoding: str = "utf-8") -> int:
    """Copy ``char_count`` characters from lines containing ``substring``.

    Args:
        source: Path to the input text file.
        destination: Path to the output text file.
        substring: Text that must be present in a line for it to be processed.
        char_count: Number of characters to copy from each matching line.
        encoding: Encoding used to read/write files.

    Returns:
        Number of lines that matched ``substring`` and were written.
    """

    if char_count <= 0:
        raise ValueError("The number of characters to copy must be positive.")

    matches = 0
    destination.parent.mkdir(parents=True, exist_ok=True)

    with source.open("r", encoding=encoding) as src, destination.open("w", encoding=encoding) as dst:
        for line in src:
            if substring in line:
                fragment = line[:char_count]
                if not fragment.endswith("\n"):
                    fragment += "\n"
                dst.write(fragment)
                matches += 1

    return matches


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy characters from lines containing a specific substring.")
    parser.add_argument("source", type=Path, help="Path to the input text file.")
    parser.add_argument("destination", type=Path, help="Path to the output text file.")
    parser.add_argument("substring", help="Only lines containing this text will be copied.")
    parser.add_argument("char_count", type=int, help="Number of characters to copy from each matching line.")
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="File encoding used for reading/writing. Defaults to UTF-8.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    matches = copy_characters(args.source, args.destination, args.substring, args.char_count, encoding=args.encoding)
    print(f"Copied {matches} matching lines to {args.destination}.")


if __name__ == "__main__":
    main()
