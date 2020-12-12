from math import floor
from copy import copy
from typing import DefaultDict, Dict, List, Tuple, Optional
import os
import re

def compute_part_1(input: str, interval: int) -> int:
	adapters = list(map(int, input.split("\n")))
	# rows = input.split("\n")

	# def is_valid(target_index: int) -> bool:
	# 	for x_index in range(target_index - interval, target_index):
	# 		for y_index in range(target_index - interval, target_index):
	# 			if x_index == y_index:
	# 				continue

	# 			if rows[x_index] + rows[y_index] == rows[target_index]:
	# 				return True
		
	# 	return False

	current_joltage = 0

	diffs = {}

	while adapters:
		# for adapter in copy(adapters):

		adapter = min(adapters)
		if adapter - current_joltage <= 3:
			diff = adapter - current_joltage

			diffs[diff] = diffs.get(diff, 0) + 1

			adapters.remove(adapter)
			current_joltage = adapter

	return diffs

def compute_part_2(input: str, interval: int, invalid_number: int) -> int:
	return 0

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day10_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	interval = 25
	print(invalid_number := compute_part_1(input, interval))
	print(compute_part_2(input, interval, invalid_number))

	return 0

if __name__ == '__main__':
	exit(main())
