import os
from typing import List, Tuple, Dict, Set

def is_valid(input: int) -> bool:
	has_double = False

	for i in range(0, 5):
		prev = int(str(input)[i - 1]) if i > 0 else None
		left = int(str(input)[i])
		right = int(str(input)[i + 1])
		next = int(str(input)[i + 2]) if i < 4 else None

		if left > right:
			return False

		if left == right and left != prev and left != next:
			has_double = True

	return has_double
	

def compute_part_1(input: str) -> int:
	count = 0
	for i in range(254032, 789860):
		if is_valid(i):
			count += 1
	
	return count
	# inputs = parse_input(input)

	# path1 = plot2(inputs[0])
	# path2 = plot2(inputs[1])

	# intersections = path1.keys() & path2.keys()
	# distances = [abs(position[0]) + abs(position[1]) for position in intersections]

	# return min(distances)


def compute_part_2(input: str) -> int:
	return 1
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
	print(f"part1: {compute_part_1(input)}")
	print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())