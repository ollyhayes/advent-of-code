from math import floor
from typing import DefaultDict, Dict, List, Tuple, Optional
import os
import re

def compute_part_1(input: str, interval: int) -> int:
	rows = list(map(int, input.split("\n")))
	# rows = input.split("\n")

	def is_valid(target_index: int) -> bool:
		for x_index in range(target_index - interval, target_index):
			for y_index in range(target_index - interval, target_index):
				if x_index == y_index:
					continue

				if rows[x_index] + rows[y_index] == rows[target_index]:
					return True
		
		return False

	for target_index in range(interval, len(rows)):
		if not is_valid(target_index):
			return rows[target_index]

	raise Exception()

def compute_part_2(input: str, interval: int, invalid_number: int) -> int:
	rows = list(map(int, input.split("\n")))

	def is_valid(target_index: int) -> Optional[Tuple[int, int]]:
		total = rows[target_index]
		for x_index in range(target_index + 1, len(rows)):
			total += rows[x_index]
			if total == invalid_number:
				return target_index, x_index
		
		return None

	for target_index in range(0, len(rows)):
		result = is_valid(target_index)
		if result:
			operands = rows[result[0]:result[1]]
			return min(operands) + max(operands)

	raise Exception()

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day09_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	interval = 25
	print(invalid_number := compute_part_1(input, interval))
	print(compute_part_2(input, interval, invalid_number))

	return 0

if __name__ == '__main__':
	exit(main())
