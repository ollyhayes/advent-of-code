import os
from math import atan, pi
from copy import copy
import sys, tty, termios
import asyncio
from asyncio import Queue, gather
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Protocol
from itertools import zip_longest
from dataclasses import dataclass, field

def find_highest_common_factor(x: int, y: int) -> int:
	highest_common_factor = 1

	for factor in sorted(range(1, x + 1), reverse=True):
		factor_multiplied = factor
		is_x_factor = False
		is_y_factor = False

		while factor_multiplied <= y:
			if factor_multiplied == x:
				is_x_factor = True
			if factor_multiplied == y:
				is_y_factor = True

			factor_multiplied += factor

		if is_x_factor and is_y_factor:
			highest_common_factor = factor
			break
	
	return highest_common_factor

def simplify_fraction(x: int, y: int) -> Tuple[int, int]:
	if x == 0:
		return 0, y // abs(y)
	if y == 0:
		return x // abs(x), 0
	if x == y:
		return x // abs(x), y // abs(y)
	if abs(x) > abs(y):
		y, x = simplify_fraction(y, x)
		return x, y

	highest_common_factor = find_highest_common_factor(abs(x), abs(y))

	return x // highest_common_factor, y // highest_common_factor

def get_angle(position: Tuple[int, int]) -> float:
	if position[0] == 0:
		return 0 if position[1] < 0 else pi
	
	angle = atan(position[1] / position[0])

	return angle + (pi / 2 if position[0] > 0 else 3 * pi / 2)

def calculate_hits(rows: List[str], x_pos: int, y_pos: int, height: int, width: int) -> Dict[float, List[Tuple[int, int]]]:
	hits: Dict[float, List[Tuple[int, int]]] = {}

	for y_tar in range(0, height):
		for x_tar in range(0, width):
			if rows[y_tar][x_tar] == ".":
				continue

			x_diff = x_tar - x_pos
			y_diff = y_tar - y_pos

			if x_diff == 0 and y_diff == 0:
				continue

			# direction = simplify_fraction((x_diff, y_diff))
			direction = get_angle((x_diff, y_diff))

			hits[direction] = hits.get(direction, []) + [(x_diff, y_diff)]

	return hits

def compute_part_1(input: str) -> Tuple[Tuple[int, int], int]:
	rows = input.split("\n")
	width = len(rows[0])
	height = len(rows)

	max_asteroids_detected = 0
	best_position: Tuple[int, int] = (-1,-1)

	for y_pos in range(0, height):
		for x_pos in range(0, width):
			if rows[y_pos][x_pos] == ".":
				continue

			hits = calculate_hits(rows, x_pos, y_pos, width, height)
			
			astroids_detected = len(hits)

			if astroids_detected > max_asteroids_detected:
				max_asteroids_detected = astroids_detected
				best_position = (x_pos, y_pos)
	
	return best_position, max_asteroids_detected

def compute_part_2(input: str, x_pos: int, y_pos: int, nth_asteroid: int) -> Tuple[int, int]:
	rows = input.split("\n")
	width = len(rows[0])
	height = len(rows)

	hits = calculate_hits(rows, x_pos, y_pos, width, height)

	for angle, positions in hits.items():
		hits[angle] = sorted(positions, key=lambda position: position[0] * position[0] + position[1] * position[1], reverse=True)

	nth = 1
	print_grid(rows, x_pos, y_pos, "|")

	while hits:
		ordered_hits = sorted(hits.keys())
		
		for angle in ordered_hits:
			positions2 = hits.get(angle)

			if positions2:
				position = positions2.pop()
			else:
				continue

			# print_grid(rows, x_pos + position[0], y_pos + position[1], "█")

			if nth == nth_asteroid:
				return (position[0] + x_pos, position[1] + y_pos)

			nth += 1

	raise Exception("not found")

def print_grid(rows: List[str], x_pos: int, y_pos: int, char: str) -> None:

	for y in range(0, len(rows)):
		if y == y_pos:
			as_list = list(rows[y_pos])
			as_list[x_pos] = char
			rows[y_pos] = "".join(as_list)

		print(rows[y])

	print()


def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day10_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input, 26, 29, 200))

	return 0

if __name__ == '__main__':
	exit(main())
