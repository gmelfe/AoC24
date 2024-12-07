import argparse
from typing import List


def read_input(file_name: str) -> List[List[int]]:
    """Read a list of reports from the input file. Each report is a list of numbers.
    There is one report per line in the input file.
    """
    with open(file_name, "r") as file:
        return [list(map(int, line.split())) for line in file]


def check_all_increasing(numbers: List[int]) -> bool:
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True


def within_safe_distance(report: List[int]) -> bool:
    """Check if two consecutive numbers are within 3 of each other."""
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) > 3:
            return False
    return True


def count_safe_reports(reports: List[List[int]], debug=False) -> int:
    safe_reports = 0
    for report in reports:
        if debug:
            print(report)
        if check_all_increasing(report) or check_all_increasing(report[::-1]):
            if debug:
                print("increasing or decreasing")
            if within_safe_distance(report):
                safe_reports += 1
        elif debug:
            print("Mixed or equal")
    return safe_reports


# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="Day 02", description="Solution to day 02 of the Advent of Code 2024."
)
parser.add_argument(
    "input_file",
    help="Input file",
    default="./input.txt",
)
parser.add_argument(
    "--debug",
    "-d",
    help="Print debug information",
    action="store_true",
)
args = parser.parse_args()

# Read input data
reports = read_input(args.input_file)

# Part 1
print(count_safe_reports(reports, args.debug))

# Part 2
