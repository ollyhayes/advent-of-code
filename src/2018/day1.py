import os
from typing import List, Tuple, Dict, Set

def compute_part_1(input: str) -> int:
	return int(input)
	# inputs = parse_input(input)

	# path1 = plot2(inputs[0])
	# path2 = plot2(inputs[1])

	# intersections = path1.keys() & path2.keys()
	# distances = [abs(position[0]) + abs(position[1]) for position in intersections]

	# return min(distances)


def compute_part_2(input: str) -> int:
	return int(input)
	# inputs = parse_input(input)

	# path1 = plot2(inputs[0])
	# path2 = plot2(inputs[1])

	# intersection_points = path1.keys() & path2.keys()

	# distances = [
	# 	path1[intersection_point] + path2[intersection_point]
	# 	for intersection_point
	# 	in intersection_points
	# ]

	# return min(distances) + 2

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