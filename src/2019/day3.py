import os
from typing import List, Tuple, Dict, Set

def parse_input(input_raw: str) -> List[List[Tuple[str, int]]]:
	return [
		[(command[0], int(command[1:])) for command in path.split(",")]
		for path
		in input_raw.split("\n")
	]

world_radius = 250
origin = world_radius, world_radius
world = [[0] * world_radius * 2 for i in range(0, world_radius * 2)]

def inc_point(world, position, value):
	x, y = position
	value = world[x][y] 
	world[x][y] = value + 1
	# print(f"set point: {x},{y} to {value + 1}")
	return value + 1

def plot(input: List[Tuple[str, int]], world) -> List[Tuple[int, int]]:
	position = origin
	inc_point(world, position, 1)
	intersections_found: List[Tuple[int, int]] = []

	for direction, length in input:
		direction_parts = directions[direction]

		for _ in range(0, length):
			position = position[0] + direction_parts[0], position[1] + direction_parts[1]
			new_value = inc_point(world, position, 1)

			if new_value == 2:
				print(f"intersection found: {position[0] - world_radius}, {position[1] - world_radius}")
				intersections_found.append(position)
	
	return intersections_found

directions: Dict[str, Tuple[int, int]] = {
	"R": (1,0),
	"L": (-1,0),
	"U": (0,1),
	"D": (0,-1),
}

def plot2(input: List[Tuple[str, int]]) -> Set[Tuple[int, int]]:
	occupied_positions: Set[Tuple[int, int]] = set()
	position: Tuple[int, int] = (0, 0)

	for direction, length in input:
		direction_parts = directions[direction]

		for _ in range(0, length):
			position = position[0] + direction_parts[0], position[1] + direction_parts[1]
			occupied_positions.add(position)

	return occupied_positions


def compute_part_1(input: str) -> int:
	inputs = parse_input(input)

	path1 = plot2(inputs[0])
	path2 = plot2(inputs[1])

	intersections = path1 & path2
	distances = [abs(position[0]) + abs(position[1]) for position in intersections]

	return min(distances)

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day3_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(f"part1: {compute_part_1(input)}")
	# print(f"part2: {compute_part_2(input, 19690720)}")

	return 0

if __name__ == '__main__':
	exit(main())

# plot(test_input[0], world)
# plot(test_input[1], world)

# for line in world:
# 	row = ""
# 	for field in line:
# 		row += str(field)

# 	print(row)

# would have been much easier to just build up a set of visited values, and then find the intersections