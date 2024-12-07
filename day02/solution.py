import argparse
from typing import List


def read_input(file_name: str) -> List[List[int]]:
    """Read a list of reports from the input file. Each report is a list of numbers.
    There is one report per line in the input file.
    """
    with open(file_name, "r") as file:
        return [list(map(int, line.split())) for line in file]


def check_all_increasing(numbers: List[int]):
    """Check if all numbers in a list are increasing.
    If they are not, return False together with the index of the first number that is not increasing.
    """
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False, i
    return True, -1


def within_safe_distance(report: List[int]):
    """Check if two consecutive numbers are within 3 of each other.
    If they are not, return False together with the index of the first number that is not within 3 of the previous.
    """
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) > 3:
            return False, i
    return True, -1


def count_safe_reports(
    reports: List[List[int]], tolerance: int = 0, debug: bool = False
) -> int:
    safe_reports = 0
    for report in reports:
        operations = 0
        is_report_safe = False
        solution_space = [report]
        if debug:
            print(f"\nReport: {report}")
        while not is_report_safe and len(solution_space) > 0:
            is_distance_safe = True
            if debug:
                print(f"Solution space: {solution_space}")
            report = solution_space.pop(0)
            is_increasing, fail_idx_inc = check_all_increasing(report)
            is_decreasing, fail_idx_dec = check_all_increasing(report[::-1])
            if debug:
                print(f"Trying solution: {report}")
                print(f"\tis_increasing={is_increasing} (error_index={fail_idx_inc})")
                print(f"\tis_decreasing={is_decreasing} (error_index={fail_idx_dec})")
            if is_increasing or is_decreasing:
                is_distance_safe, fail_idx_dist = within_safe_distance(report)
                if debug:
                    print(
                        f"\tis_distance_safe={is_distance_safe} (error_index={fail_idx_dist})"
                    )
                if is_distance_safe:
                    is_report_safe = True
                    safe_reports += 1
            if not is_report_safe and operations < tolerance:
                if not is_increasing:
                    new_solution = report.copy()
                    new_solution.pop(fail_idx_inc - 1)
                    solution_space.append(new_solution)
                    new_solution = report.copy()
                    new_solution.pop(fail_idx_inc)
                    solution_space.append(new_solution)
                    new_solution = report.copy()
                if not is_decreasing:
                    new_solution = report.copy()
                    new_solution.pop(fail_idx_dec - 1)
                    solution_space.append(new_solution)
                    new_solution = report.copy()
                    new_solution.pop(fail_idx_dec)
                    solution_space.append(new_solution)
                    new_solution = report.copy()
                if not is_distance_safe:
                    new_solution = report.copy()
                    new_solution.pop(fail_idx_dist - 1)
                    solution_space.append(new_solution)
                    new_solution = report.copy()
                    new_solution.pop(fail_idx_dist)
                    solution_space.append(new_solution)
                    new_solution = report.copy()
                operations += 1
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
print(count_safe_reports(reports, 0, args.debug))

# Part 2
print(count_safe_reports(reports, 1, args.debug))

# Done
