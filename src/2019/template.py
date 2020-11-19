import os
from typing import List, Tuple, Dict, Set, Callable, Optional, Union

def compute_part_1(input: str) -> int:
	output = 0

	for line in input.split("\n"):
		output += len(line)
	
	return output

def compute_part_2(input: str) -> int:
	return 1

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "dayX_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(f"part1: {compute_part_1(input)}")
	# print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())
