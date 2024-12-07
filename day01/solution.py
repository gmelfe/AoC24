import argparse


def read_input(file_name):
    """Reads two lists of numbers from the input text file.

    Each line in the file contains two numbers separated by one or more spaces,
    corresponding to the elements of two separate lists.
    """
    list_one = []
    list_two = []
    with open(file_name, "r") as file:
        for line in file:
            number_one, number_two = map(int, line.split())
            list_one.append(number_one)
            list_two.append(number_two)
    return list_one, list_two


def calculate_distance(numbers_a, numbers_b):
    """Calculate the sum of the absolute differences between the elements of two sorted lists."""
    return sum(
        abs(num_a - num_b) for num_a, num_b in zip(sorted(numbers_a), sorted(numbers_b))
    )


def similarity_score(numbers_a, numbers_b):
    """Calculate the sum of the products of each number in the first list by its count in the second list."""
    return sum(num_a * numbers_b.count(num_a) for num_a in numbers_a)


# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="Day 01", description="Solution to day 01 of the Advent of Code 2024."
)
parser.add_argument(
    "input_file",
    help="Input file",
    default="./input.txt",
)
args = parser.parse_args()

# Read input data
l1, l2 = read_input(args.input_file)

# Part 1
output_part1 = calculate_distance(l1, l2)
print(output_part1)

# Part 2
output_part2 = similarity_score(l1, l2)
print(output_part2)
