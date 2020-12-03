from math import floor
from typing import List
import os

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	lines = input.split("\n")

	trees = 0
	opens = 0
	position = (0, 0)

	for line in lines:
		position = add(position, (3, 1))
		
		val = lines[position[1]][position[0]]

		if val == "#":
			trees += 1
		else:
			opens += 1

	print(trees)
	print(opens)

	return 0

def add(x, y):
	return x[0] + y[0], x[1] + y[1]

def compute_part_2(input: str) -> int:
	pass

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day3_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
