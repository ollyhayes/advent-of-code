from math import floor, sin, cos, pi, sqrt, atan
from typing import Dict, List, Tuple, Optional, Callable
import os

Vector = Tuple[float, float]

def add(x: Vector, y: Vector) -> Vector:
	return x[0] + y[0], x[1] + y[1]

def subtract(x: Vector, y: Vector) -> Vector:
	return x[0] - y[0], x[1] - y[1]

def multiply(x: Vector, y: float) -> Vector:
	return x[0] * y, x[1] * y

def calculate_angle(vector: Vector) -> float:
	if vector[0] == 0:
		return -pi / 2 if vector[1] < 0 else pi / 2
	
	angle = atan(vector[1] / vector[0])

	return angle if vector[0] > 0 else angle + pi

def calculate_vector(direction: float, magnitude: float) -> Vector:
	return magnitude * cos(direction), magnitude * sin(direction)

def magnitude(vector: Vector) -> float:
	return sqrt(vector[0] * vector[0] + vector[1] * vector[1])

def compute_part_1(input: str) -> float:
	# rows = list(map(float, input.split("\n")))
	rows = input.split("\n")
	position, direction = (0,0), 0

	def move_in_direction(position_diff: Tuple[float,float]):
		def move_inner(position: Vector, direction: float, value: float) -> Tuple[Vector, float]:
			return add(position, multiply(position_diff, value)), direction
		return move_inner

	def turn(direction_diff: float):
		def turn_inner(position: Vector, direction: float, value: float) -> Tuple[Vector, float]:
			return position, direction + direction_diff * (value * pi / 180)
		return turn_inner

	def go_forward(position: Vector, direction: float, value: float) -> Tuple[Vector, float]:
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
	position, waypoint_vector = (0,0), (10, -1)

	def move_in_direction(position_diff: Tuple[float,float]):
		def move_inner(position: Vector, waypoint_vector: Tuple[float,float], value: float) -> Tuple[Vector, Vector]:
			return position, add(waypoint_vector, multiply(position_diff, value))
		return move_inner

	def turn(direction_diff: float):
		def turn_inner(position: Vector, waypoint_vector: Vector, value: float) -> Tuple[Vector, Vector]:
			angle_to_waypofloat = calculate_angle(waypoint_vector)
			distance_to_waypoint = magnitude(waypoint_vector)

			new_angle_to_paypofloat = angle_to_waypofloat + direction_diff * (value * pi / 180)

			return position, calculate_vector(new_angle_to_paypofloat, distance_to_waypoint)

		return turn_inner

	def go_forward(position: Vector, waypoint_vector: Vector, value: float) -> Tuple[Vector, Vector]:
		diff = multiply(waypoint_vector, value)

		return add(position, diff), waypoint_vector

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

		position, waypoint_vector = ops[command](position, waypoint_vector, value)

		# print(f"row: {row}, pos: {position}, way: {waypoint_vector}")

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
