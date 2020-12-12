from math import floor, sin, cos, pi, sqrt, atan
from typing import Dict, List, Tuple, Optional, Callable
import os

def add(x: Tuple[int, int], y: Tuple[int, int]):
	return x[0] + y[0], x[1] + y[1]

def subtract(x: Tuple[int, int], y: Tuple[int, int]):
	return x[0] - y[0], x[1] - y[1]

def multiply(x: Tuple[int, int], y: int):
	return x[0] * y, x[1] * y

def get_angle(position: Tuple[int, int]) -> float:
	if position[0] == 0:
		return -pi / 2 if position[1] < 0 else pi / 2
	
	angle = atan(position[1] / position[0])

	return angle if position[0] > 0 else angle + pi

	# return angle


def get_position_diff(direction: int, value: int) -> Tuple[int, int]:
	rad = direction * pi / 180
	return round(value * cos(rad)), round(value * sin(rad))

def compute_part_1(input: str) -> int:
	# rows = list(map(int, input.split("\n")))
	rows = input.split("\n")
	position, direction = (0,0), 0

	def move_in_direction(position_diff: Tuple[int,int]):
		def move_inner(position: Tuple[int, int], direction: int, value: int) -> Tuple[Tuple[int, int], int]:
			return add(position, multiply(position_diff, value)), direction
		return move_inner

	def turn(direction_diff: int):
		def turn_inner(position: Tuple[int, int], direction: int, value: int) -> Tuple[Tuple[int, int], int]:
			return position, direction + direction_diff * value
		return turn_inner

	def go_forward(position: Tuple[int, int], direction: int, value: int) -> Tuple[Tuple[int, int], int]:
		return add(position, get_position_diff(direction, value)), direction

	ops: Dict[str, Callable] = {
		"N": move_in_direction((0, -1)),
		"S": move_in_direction((0, 1)),
		"E": move_in_direction((1, 0)),
		"W": move_in_direction((-1, 0)),
		"L": turn(-1),
		"R": turn(1),
		"F": go_forward,
	}

	for row in rows:
		command = row[:1]
		value = int(row[1:])

		position, direction = ops[command](position, direction, value)

		# print(f"row: {row}, pos: {position}, dir: {direction}")

	return abs(position[0]) + abs(position[1])

def compute_part_2(input: str) -> int:
	# rows = list(map(int, input.split("\n")))
	rows = input.split("\n")
	position, waypoint_position = (0,0), (10, -1)

	def move_in_direction(position_diff: Tuple[int,int]):
		def move_inner(position: Tuple[int, int], waypoint_position: Tuple[int,int], value: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
			return position, add(waypoint_position, multiply(position_diff, value))
		return move_inner

	def turn(direction_diff: int):
		def turn_inner(position: Tuple[int, int], waypoint_position: Tuple[int, int], value: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
			angle_to_waypoint = round(get_angle(waypoint_position) * 180 / pi)
			distance_to_waypoint = round(sqrt(waypoint_position[0] * waypoint_position[0] + waypoint_position[1] * waypoint_position[1]))

			new_angle_to_paypoint = angle_to_waypoint + direction_diff * value

			return position, get_position_diff(new_angle_to_paypoint, distance_to_waypoint)

		return turn_inner

	def go_forward(position: Tuple[int, int], waypoint_position: Tuple[int, int], value: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
		diff = multiply(waypoint_position, value)

		return add(position, diff), waypoint_position

	ops: Dict[str, Callable] = {
		"N": move_in_direction((0, -1)),
		"S": move_in_direction((0, 1)),
		"E": move_in_direction((1, 0)),
		"W": move_in_direction((-1, 0)),
		"L": turn(-1),
		"R": turn(1),
		"F": go_forward,
	}

	for row in rows:
		command = row[:1]
		value = int(row[1:])

		position, waypoint_position = ops[command](position, waypoint_position, value)

		print(f"row: {row}, pos: {position}, way: {waypoint_position}")

	return abs(position[0]) + abs(position[1])

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	# test_pos = [
	# 	(1,0),
	# 	(2,1),
	# 	(1,1),
	# 	(1,2),
	# 	(0,1),
	# 	(-1,1),
	# 	(-1,0),
	# 	(-1,-1),
	# 	(0,-1),
	# 	(1,-1),
	# ]
	# print([get_position_diff(int(get_angle(pos) * 180 / pi), 10) for pos in test_pos])
	# exit(0)
	exit(main())
