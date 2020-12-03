from math import floor
from typing import List, Tuple
import os

def compute_part_1(input: str, direction: Tuple[int, int]) -> int:
	# lines = list(map(int, input.split("\n")))
	lines = input.split("\n")

	width = len(lines[0])

	trees = 0
	opens = 0
	position = (0, 0)

	while position[1] < len(lines):
		val = lines[position[1]][position[0]]

		if val == "#":
			trees += 1
		else:
			opens += 1

		position = add(position, direction, width)

		# if position[0] > width:
		# 	position = (position[0] - width, position[1])
		
	print(trees)
	print(opens)

	return trees

def add(x, y, width):
	return (x[0] + y[0]) % width, x[1] + y[1]

def compute_part_2(input: str) -> int:
	slopes = [
		(1, 1),
		(3, 1),
		(5, 1),
		(7, 1),
		(1, 2),
	]
	total_trees_multiplied = 1

	for slope in slopes:
		trees = compute_part_1(input, slope)
		total_trees_multiplied *= trees

	return total_trees_multiplied

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day3_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input, (3, 1)))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
