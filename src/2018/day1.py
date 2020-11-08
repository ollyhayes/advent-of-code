import os
from typing import List, Tuple, Dict, Set

def compute_part_1(input: str) -> int:
	operations = input.split("\n")
	frequency = 0

	for operation in operations:
		operator = operation[:1]
		value = int(operation[1:])

		if operator == "+":
			frequency += value
		elif operator == "-":
			frequency -= value
	
	return frequency

def compute_part_2(input: str) -> int:
	operations = input.split("\n")

	frequency = 0
	reached_frequencies = set()

	while True:
		for operation in operations:
			operator = operation[:1]
			value = int(operation[1:])

			if operator == "+":
				frequency += value
			elif operator == "-":
				frequency -= value
			
			if frequency in reached_frequencies:
				return frequency

			reached_frequencies.add(frequency)

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day1_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(f"part1: {compute_part_1(input)}")
	print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())