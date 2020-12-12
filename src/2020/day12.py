from math import floor, sin, cos, pi, sqrt, atan
from typing import Dict, List, Tuple, Optional, Callable
import os

def add(x: Tuple[float, float], y: Tuple[float, float]):
	return x[0] + y[0], x[1] + y[1]

def subtract(x: Tuple[float, float], y: Tuple[float, float]):
	return x[0] - y[0], x[1] - y[1]

def multiply(x: Tuple[float, float], y: float):
	return x[0] * y, x[1] * y

def calculate_angle(position: Tuple[float, float]) -> float:
	if position[0] == 0:
		return -pi / 2 if position[1] < 0 else pi / 2
	
	angle = atan(position[1] / position[0])

	return angle if position[0] > 0 else angle + pi

def calculate_vector(direction: float, value: float) -> Tuple[float, float]:
	return value * cos(direction), value * sin(direction)

def compute_part_1(input: str) -> float:
	# rows = list(map(float, input.split("\n")))
	rows = input.split("\n")
	position, direction = (0,0), 0

	def move_in_direction(position_diff: Tuple[float,float]):
		def move_inner(position: Tuple[float, float], direction: float, value: float) -> Tuple[Tuple[float, float], float]:
			return add(position, multiply(position_diff, value)), direction
		return move_inner

	def turn(direction_diff: float):
		def turn_inner(position: Tuple[float, float], direction: float, value: float) -> Tuple[Tuple[float, float], float]:
			return position, direction + direction_diff * (value * pi / 180)
		return turn_inner

	def go_forward(position: Tuple[float, float], direction: float, value: float) -> Tuple[Tuple[float, float], float]:
		return add(position, calculate_vector(direction, value)), direction

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
		value = float(row[1:])

		position, direction = ops[command](position, direction, value)

		# print(f"row: {row}, pos: {position}, dir: {direction}")

	return round(abs(position[0]) + abs(position[1]))

def compute_part_2(input: str) -> float:
	# rows = list(map(float, input.split("\n")))
	rows = input.split("\n")
	position, waypoint_position = (0,0), (10, -1)

	def move_in_direction(position_diff: Tuple[float,float]):
		def move_inner(position: Tuple[float, float], waypoint_position: Tuple[float,float], value: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
			return position, add(waypoint_position, multiply(position_diff, value))
		return move_inner

	def turn(direction_diff: float):
		def turn_inner(position: Tuple[float, float], waypoint_position: Tuple[float, float], value: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
			angle_to_waypofloat = calculate_angle(waypoint_position)
			distance_to_waypoint = sqrt(waypoint_position[0] * waypoint_position[0] + waypoint_position[1] * waypoint_position[1])

			new_angle_to_paypofloat = angle_to_waypofloat + direction_diff * (value * pi / 180)

			return position, calculate_vector(new_angle_to_paypofloat, distance_to_waypoint)

		return turn_inner

	def go_forward(position: Tuple[float, float], waypoint_position: Tuple[float, float], value: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
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
		value = float(row[1:])

		position, waypoint_position = ops[command](position, waypoint_position, value)

		# print(f"row: {row}, pos: {position}, way: {waypoint_position}")

	return round(abs(position[0]) + abs(position[1]))

def main() -> float:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
