from math import floor
from typing import List
import os

def compute_part_1(input: str) -> int:
	lines = list(map(int, input.split("\n")))
	# lines = input.split("\n")

	for x in lines:
		for y in lines:
				if x + y == 2020:
					return x * y
	return 0

def compute_part_2(input: str) -> int:
	lines = list(map(int, input.split("\n")))
	# lines = input.split("\n")

	for x in lines:
		for y in lines:
			for z in lines:
				if x + y + z == 2020:
					return x * y * z
	return 0

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day1_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
