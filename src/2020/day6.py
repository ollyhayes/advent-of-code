from math import floor
from typing import DefaultDict, Dict, List, Tuple
import os

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	groups = input.split("\n\n")

	summed_group_yes_answers = 0

	for group in groups:
		people = group.split("\n")

		group_yes_answers = set()

		for person in people:
			group_yes_answers |= set(person)
		
		summed_group_yes_answers += len(group_yes_answers)

	return summed_group_yes_answers

def compute_part_2(input: str) -> int:
	groups = input.split("\n\n")

	summed_group_yes_answers = 0

	for group in groups:
		people = group.split("\n")

		group_yes_answers = set(people[0])
		
		for person in people:
			group_yes_answers &= set(person)

		summed_group_yes_answers += len(group_yes_answers)

	return summed_group_yes_answers

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day6_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
