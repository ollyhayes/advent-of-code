from math import floor
from copy import deepcopy
from typing import Dict, List, Tuple, Optional
import os

Vector = Tuple[int, int]

def add(x: Vector, y: Vector) -> Vector:
	return x[0] + y[0], x[1] + y[1]

def multiply(x: Vector, y: int) -> Vector:
	return x[0] * y, x[1] * y

def compute(input: str, uncomfortable_neighbour_count: int, look_through_empties: bool) -> int:
	rows = [list(row) for row in input.split("\n")]
	width = len(rows[0])
	height = len(rows)

	surroundings: List[Vector] = [
		(1,1),
		(1,0),
		(1,-1),
		(0,1),
		(0,-1),
		(-1,1),
		(-1,0),
		(-1,-1),
	]

	def is_occupied(rows: List[List[str]], position: Vector, direction: Vector, magnitude: int = 1) -> bool:
		target_position = add(position, multiply(direction, magnitude))

		if not 0 <= target_position[0] < width or not 0 <= target_position[1] < height:
			return False

		seat = rows[target_position[1]][target_position[0]]
		
		if seat == "#":
			return True
		elif seat == "L":
			return False
		elif not look_through_empties:
			return False
		else:
			return is_occupied(rows, position, direction, magnitude + 1)

	def apply_round(rows: List[List[str]]) -> Tuple[List[List[str]], int]:
		next_round = deepcopy(rows)
		change_count = 0

		for y in range(0, height):
			for x in range(0, width):
				seat = rows[y][x]
				if seat == ".":
					continue

				occupied_count = sum(is_occupied(rows, (x,y), surrounding) for surrounding in surroundings)

				if seat == "L" and occupied_count == 0:
					next_round[y][x] = "#"
					change_count += 1
				elif seat == "#" and occupied_count >= uncomfortable_neighbour_count:
					next_round[y][x] = "L"
					change_count += 1

		return next_round, change_count
	
	while True:
		rows, count = apply_round(rows)
		if count == 0:
			break

	# for row in rows:
	# 	print("".join(row))

	occupied = sum(seat == "#" for row in rows for seat in row)

	return occupied

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute(input, 4, False))
	print(compute(input, 5, True))

	return 0

if __name__ == '__main__':
	exit(main())
