import os
from copy import copy
import sys, tty, termios
import asyncio
from asyncio import Queue, gather
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Protocol
from itertools import zip_longest
from dataclasses import dataclass, field

def compute_part_1(input: str) -> Tuple[Tuple[int, int], int]:
	rows = input.split("\n")
	WIDTH = len(rows[0])
	HEIGHT = len(rows)

	max_asteroids_detected = 0
	best_position: Tuple[int, int] = (-1,-1)

	for y_pos in range(0, HEIGHT):
		for x_pos in range(0, WIDTH):
			if rows[y_pos][x_pos] == ".":
				continue

			hits: Dict[Tuple[int, int], int] = {}

			for y_tar in range(0, HEIGHT):
				for x_tar in range(0, WIDTH):
					if rows[y_tar][x_tar] == ".":
						continue

					x_diff = x_tar - x_pos
					y_diff = y_tar - y_pos

					if x_diff == 0 and y_diff == 0:
						continue

					direction = simplify_fraction(x_diff, y_diff)

					hits[direction] = hits.get(direction, 0) + 1

					# if hits[direction] > 1 and y_tar != 0:
					# 	print('ah')
			
			astroids_detected = len(hits)

			if astroids_detected > max_asteroids_detected:
				max_asteroids_detected = astroids_detected
				best_position = (x_pos, y_pos)
	
	return best_position, max_asteroids_detected

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
		return 0, y // y
	if y == 0:
		return x // x, 0
	if x == y:
		return x // x, y // y
	if abs(x) > abs(y):
		y, x = simplify_fraction(y, x)
		return x, y

	highest_common_factor = find_highest_common_factor(abs(x), abs(y))

	return x // highest_common_factor, y // highest_common_factor

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day10_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	compute_part_1(input)

	return 0

if __name__ == '__main__':
	print(simplify_fraction(-28, 4))
	# exit(main())
