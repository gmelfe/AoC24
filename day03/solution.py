import argparse
import re
from typing import List, Tuple


def read_input(file_name: str) -> str:
    """Read all lines from the input file into a huge string"""
    with open(file_name, "r") as file:
        return file.read()


def parse_instructions(instructions: str) -> List[Tuple[str, str]]:
    """Find all matches of the pattern mul(x,y) in the instructions string,
    where x and y are integers, and return a list of tuples (x,y).
    """
    return re.findall(r"mul\((\d+),(\d+)\)", instructions)


def sum_multiplications(multiplications: List[Tuple[str, str]]) -> int:
    """Compute the sum of all multiplications in the list of tuples (x,y)."""
    return sum(int(x) * int(y) for x, y in multiplications)


# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="Day 03", description="Solution to day 03 of the Advent of Code 2024."
)
parser.add_argument(
    "input_file",
    help="Input file",
    default="./input.txt",
)
args = parser.parse_args()

# Read input data
instructions = read_input(args.input_file)

# Part 1
multiplications = parse_instructions(instructions)
print(sum_multiplications(multiplications))

# Part 2

# Done
