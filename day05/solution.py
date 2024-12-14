import argparse
from collections import defaultdict
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
    rules: List[List[int]],
    oders: List[List[int]],
    debug: bool = False,
    fix_orders: bool = False,
) -> int:
    sum = 0
    for order in orders:
        violated_rules = []
        for rule in rules:
            try:
                idx_a = order.index(rule[0])
                idx_b = order.index(rule[1])
                if idx_a > idx_b:
                    violated_rules.append(rule)
            except ValueError:
                pass
        if debug and len(violated_rules) > 0:
            print(f"Order: {order}")
            print(f"Invalid, violates rules: {violated_rules}")
        if len(violated_rules) > 0 and fix_orders:
            master_order = get_ordered_integers(rules)
            fixed_order = []
            for element in master_order:
                if element in order:
                    fixed_order.append(element)
            mid_element = fixed_order[len(fixed_order) // 2]
            if debug:
                print(f"Fixed: {fixed_order}")
                print(f"Valid. Middle element: {mid_element}")
            sum += mid_element
        if len(violated_rules) == 0 and not fix_orders:
            mid_element = order[len(order) // 2]
            if debug:
                print(f"Order: {order}")
                print(f"Valid. Middle element: {mid_element}")
            sum += mid_element
    return sum


def get_ordered_integers(rules):
    # Create a graph representation using adjacency list
    graph = defaultdict(list)
    nodes = set()
    for a, b in rules:
        graph[a].append(b)
        nodes.add(a)
        nodes.add(b)

    # Create a set to keep track of visited nodes
    visited = set()

    # Create a list to store the ordered integers
    ordered_integers = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        ordered_integers.append(node)

    # Perform depth-first search (DFS) on each node
    for node in nodes:
        if node not in visited:
            dfs(node)

    # Reverse the order of integers to get the correct ordering
    ordered_integers.reverse()

    return ordered_integers


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
print(verify_orders(rules, orders, args.debug, True))

# Done
