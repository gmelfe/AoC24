import argparse
from typing import List


def read_input(file_name: str):
    """Read all characters from all lines in the input file into a huge character matrix"""
    with open(file_name, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def count_horizontally(word_search, sequence):
    count = 0
    for row in word_search:
        count += "".join(row).count(sequence)  # left to right
        count += "".join(reversed(row)).count(sequence)  # right to left
    return count


def count_diagonally(word_search, sequence):
    # WARNING: sequence length hardcoded to 4
    rows = len(word_search)
    cols = len(word_search[0])
    count = 0

    # Check forward diagonals
    for i in range(rows - 3):
        for j in range(cols - 3):
            if (
                "".join(
                    [
                        word_search[i][j],
                        word_search[i + 1][j + 1],
                        word_search[i + 2][j + 2],
                        word_search[i + 3][j + 3],
                    ]
                )
                == sequence
            ):
                count += 1

    # Check backward diagonals
    for i in range(rows - 3):
        for j in range(3, cols):
            if (
                "".join(
                    [
                        word_search[i][j],
                        word_search[i + 1][j - 1],
                        word_search[i + 2][j - 2],
                        word_search[i + 3][j - 3],
                    ]
                )
                == sequence
            ):
                count += 1

    return count


def count_sequence(word_search, sequence, debug=False):
    # Count the number of times a sequence of characters appears in the word search
    count = 0

    # Search horizontally
    hor_count = count_horizontally(word_search, sequence)
    count += hor_count

    # Search vertically
    ver_count = count_horizontally([list(row) for row in zip(*word_search)], sequence)
    count += ver_count

    # Search diagonally
    dia_count = count_diagonally(word_search, sequence)
    count += dia_count

    # Search diagonally flipped
    dif_count = count_diagonally(word_search[::-1], sequence)
    count += dif_count

    if debug:
        print("Word search:")
        for row in word_search:
            print(" ".join(row))
        print(f"Found {count} instances of {sequence}:")
        print(
            f"{hor_count} horizontal, {ver_count} vertical, {dia_count} diagonal, {dif_count} diagonal flipped"
        )

    return count


def count_xmas(word_search: List[List[str]], debug=False):
    count = 0
    if debug:
        print("Word search:")
        for row in word_search:
            print(" ".join(row))
    for i in range(len(word_search) - 2):
        for j in range(len(word_search[i]) - 2):
            if debug:
                print(f"i={i} j={j}")
            if word_search[i + 1][j + 1] == "A":
                word_1 = (
                    word_search[i][j]
                    + word_search[i + 1][j + 1]
                    + word_search[i + 2][j + 2]
                )
                word_2 = (
                    word_search[i][j + 2]
                    + word_search[i + 1][j + 1]
                    + word_search[i + 2][j]
                )
                if debug:
                    print(f"word_1={word_1} word_2={word_2}")
                if (word_1 == "MAS" or word_1 == "SAM") and (
                    word_2 == "MAS" or word_2 == "SAM"
                ):
                    count += 1
                    if debug:
                        print(f"Found XMAS at i={i} j={j}. Count={count}.")
    return count


# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="Day 04", description="Solution to day 04 of the Advent of Code 2024."
)
parser.add_argument(
    "input_file",
    help="Input file",
    default="./input.txt",
)
parser.add_argument(
    "--debug",
    "-d",
    action="store_true",
)
args = parser.parse_args()

# Read input data
word_search = read_input(args.input_file)

# Part 1
print(count_sequence(word_search, "XMAS", args.debug))

# Part 2
print(count_xmas(word_search, args.debug))

# Done
