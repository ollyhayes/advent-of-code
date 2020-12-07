from math import floor
from typing import DefaultDict, Dict, List, Tuple
import os
import re

regex = re.compile('(\d)? ?(\w* \w*) bags?')

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	rows = input.split("\n")

	total = 0

	bags: Dict[str, Dict[str, int]] = {}

	def contains_eventually(outer_bag: str, target_bag: str) -> bool:
		inner_bags = bags.get(outer_bag, {})

		return target_bag in inner_bags or any(contains_eventually(inner_bag, target_bag) for inner_bag in inner_bags.keys())

	for row in rows:
		new_rule = regex.findall(row)
		_, outer_bag = new_rule[0]
		inner_bags = new_rule[1:]

		if inner_bags[0][1] == 'no other':
			continue

		bags[outer_bag] = {name: count for count, name in inner_bags}

	for row in rows:
		new_rule = regex.findall(row)
		_, outer_bag = new_rule[0]

		if contains_eventually(outer_bag, "shiny gold"):
			total += 1

	return total


def compute_part_2(input: str) -> int:
	rows = input.split("\n")

	total = 0

	bags: Dict[str, Dict[str, int]] = {}

	def count_bags(outer_bag: str) -> int:
		inner_bags = bags.get(outer_bag, {})


		total = sum(size + size * count_bags(bag) for bag, size in inner_bags.items())
		print(f"bag: {outer_bag}, count: {total}")
		return total

		# return target_bag in inner_bags or any(contains_eventually(inner_bag, target_bag) for inner_bag in inner_bags.keys())

	for row in rows:
		new_rule = regex.findall(row)
		_, outer_bag = new_rule[0]
		inner_bags = new_rule[1:]

		if inner_bags[0][1] == 'no other':
			continue

		bags[outer_bag] = {name: int(count) for count, name in inner_bags}

	total += count_bags("shiny gold")

	return total

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day7_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
