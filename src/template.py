from math import floor
from typing import Dict, List, Tuple, Optional
import os

def compute_part_1(input: str) -> int:
	rows = list(map(int, input.split("\n")))
	# rows = input.split("\n")
	total = 0

	for row in rows:
		pass

	return total

def compute_part_2(input: str) -> int:
	rows = list(map(int, input.split("\n")))
	# rows = input.split("\n")
	total = 0

	for row in rows:
		pass

	return total

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
