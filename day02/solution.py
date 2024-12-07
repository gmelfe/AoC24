import argparse
from typing import List


def read_input(file_name: str) -> List[List[int]]:
    """Read a list of reports from the input file. Each report is a list of numbers.
    There is one report per line in the input file.
    """
    with open(file_name, "r") as file:
        return [list(map(int, line.split())) for line in file]


def check_all_increasing(numbers: List[int]) -> bool:
    """Check if all numbers in a list are increasing."""
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True


def within_safe_distance(report: List[int]):
    """Check if two consecutive numbers are within 3 of each other."""
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) > 3:
            return False
    return True


def count_safe_reports(
    reports: List[List[int]], problem_dampener: bool = False, debug: bool = False
) -> int:
    safe_reports = 0
    for report in reports:
        operations_allowed = problem_dampener
        is_report_safe = False
        solution_space = [report]
        if debug:
            print(f"\nReport: {report}")
        while not is_report_safe and len(solution_space) > 0:
            is_distance_safe = True
            if debug:
                print(f"Solution space: {solution_space}")
            report = solution_space.pop(0)
            is_increasing = check_all_increasing(report)
            is_decreasing = check_all_increasing(report[::-1])
            if debug:
                print(f"Trying solution: {report}")
                print(f"\tis_increasing={is_increasing}")
                print(f"\tis_decreasing={is_decreasing}")
            if is_increasing or is_decreasing:
                is_distance_safe = within_safe_distance(report)
                if debug:
                    print(f"\tis_distance_safe={is_distance_safe}")
                if is_distance_safe:
                    is_report_safe = True
                    safe_reports += 1
            if not is_report_safe and operations_allowed:
                # Create a new solution space consisting of all possible list subsets of the current report
                # that we can create by removing one element
                for i in range(len(report)):
                    solution_space.append(report[:i] + report[i + 1 :])  # noqa: E203
                operations_allowed = False
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
    action="store_true",
)
args = parser.parse_args()

# Read input data
reports = read_input(args.input_file)

# Part 1
print(count_safe_reports(reports, False, args.debug))

# Part 2
print(count_safe_reports(reports, True, args.debug))

# Done
