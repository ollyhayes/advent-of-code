from math import floor
from copy import deepcopy
from typing import Dict, List, Tuple, Optional
import os

Vector = Tuple[int, int]

def add(x: Vector, y: Vector) -> Vector:
	return x[0] + y[0], x[1] + y[1]

def compute_part_1(input: str) -> int:
	rows = [list(row) for row in input.split("\n")]
	total = 0
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

	def is_occupied(rows: List[List[str]], position: Vector) -> bool:
		if not 0 <= position[0] < width or not 0 <= position[1] < height:
			return False
		
		return rows[position[1]][position[0]] == "#"

	def apply_round(rows: List[List[str]]) -> Tuple[List[List[str]], int]:
		next_round = deepcopy(rows)
		change_count = 0

		for y in range(0, height):
			for x in range(0, width):
				seat = rows[y][x]
				if seat == ".":
					continue

				occupied_count = sum(is_occupied(rows, add((x,y), surrounding)) for surrounding in surroundings)

				if seat == "L" and occupied_count == 0:
					next_round[y][x] = "#"
					change_count += 1
				elif seat == "#" and occupied_count >= 4:
					next_round[y][x] = "L"
					change_count += 1

		return next_round, change_count
	
	while True:
		rows, count = apply_round(rows)
		if count == 0:
			break
			
	for row in rows:
		print("".join(row))

	occupied = sum(seat == "#" for row in rows for seat in row)

	return occupied

def compute_part_2(input: str) -> int:
	rows = input.split("\n")
	total = 0

	for row in rows:
		pass

	return total

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
