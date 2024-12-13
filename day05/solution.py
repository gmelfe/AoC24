import argparse
from typing import List


def read_input(file_name: str):
    rules = []
    orders = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            if len(line.strip()) == 0:
                continue
            if "|" in line:
                rules.append([int(x) for x in line.split("|")])
            else:
                orders.append([int(x) for x in line.split(",")])
    return rules, orders


def verify_orders(
    rules: List[List[int]], oders: List[List[int]], debug: bool = False
) -> int:
    sum = 0
    for order in orders:
        is_order_valid = True
        if debug:
            print(f"Order: {order}")
        for rule in rules:
            try:
                idx_a = order.index(rule[0])
                idx_b = order.index(rule[1])
                if idx_a > idx_b:
                    is_order_valid = False
                    if debug:
                        print(f"Invalid order, violates rule {rule}")
            except ValueError:
                pass
        if is_order_valid:
            mid_element = order[len(order) // 2]
            if debug:
                print(f"Mid element: {mid_element}")
            sum += mid_element
    return sum


# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="Day 05", description="Solution to day 05 of the Advent of Code 2024."
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
rules, orders = read_input(args.input_file)
if args.debug:
    print("Rules:")
    for rule in rules:
        print(rule)
    print("Orders:")
    for order in orders:
        print(order)

# Part 1
print(verify_orders(rules, orders, args.debug))

# Part 2

# Done
