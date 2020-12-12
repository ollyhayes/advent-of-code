import os
from typing import List, Tuple, Dict, Set

def parse_input(input_raw: str) -> List[List[Tuple[str, int]]]:
	return [
		[(command[0], int(command[1:])) for command in path.split(",")]
		for path
		in input_raw.split("\n")
	]

directions: Dict[str, Tuple[int, int]] = {
	"R": (1,0),
	"L": (-1,0),
	"U": (0,1),
	"D": (0,-1),
}

def plot2(input: List[Tuple[str, int]]) -> Dict[Tuple[int, int], int]:
	occupied_positions: Dict[Tuple[int, int], int] = {}
	position: Tuple[int, int] = (0, 0)
	distance_travelled = 0

	for direction, length in input:
		direction_parts = directions[direction]

		for _ in range(0, length):
			position = position[0] + direction_parts[0], position[1] + direction_parts[1]
			occupied_positions[position] = distance_travelled
			distance_travelled += 1

	return occupied_positions

def compute_part_1(input: str) -> int:
	inputs = parse_input(input)

	path1 = plot2(inputs[0])
	path2 = plot2(inputs[1])

	intersections = path1.keys() & path2.keys()
	distances = [abs(position[0]) + abs(position[1]) for position in intersections]

	return min(distances)


def compute_part_2(input: str) -> int:
	inputs = parse_input(input)

	path1 = plot2(inputs[0])
	path2 = plot2(inputs[1])

	intersection_points = path1.keys() & path2.keys()

	distances = [
		path1[intersection_point] + path2[intersection_point]
		for intersection_point
		in intersection_points
	]

	return min(distances) + 2

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day03_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(f"part1: {compute_part_1(input)}")
	print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())