import argparse
import os
import random
from typing import Iterable


def generate_digit_lines(line_length: int, line_count: int) -> Iterable[str]:
    """Yield ``line_count`` strings consisting of random digits of ``line_length``."""
    digits = "0123456789"
    for _ in range(line_count):
        yield "".join(random.choice(digits) for _ in range(line_length))


def write_random_digits_file(path: str, line_length: int, line_count: int) -> None:
    """Write a file filled with random digits.

    Args:
        path: Destination file path. Parent directories are created if missing.
        line_length: Number of digits in each line.
        line_count: Number of lines to generate.
    """
    if line_length <= 0:
        raise ValueError("line_length must be positive")
    if line_count <= 0:
        raise ValueError("line_count must be positive")

    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        for line in generate_digit_lines(line_length, line_count):
            file.write(f"{line}\n")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a text file containing a specified number of lines of random "
            "digits and a specified line length."
        )
    )
    parser.add_argument(
        "output",
        help="Ścieżka do generowanego pliku wyjściowego."
    )
    parser.add_argument(
        "line_count",
        type=int,
        help="Liczba wierszy do wygenerowania."
    )
    parser.add_argument(
        "line_length",
        type=int,
        help="Długość każdego wiersza (liczba cyfr)."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    write_random_digits_file(args.output, args.line_length, args.line_count)


if __name__ == "__main__":
    main()
