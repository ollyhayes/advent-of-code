from math import floor
from typing import Dict, List, Tuple, Optional
import os
from copy import copy

def compute_part_1(input: str) -> Tuple[bool, int]:
	# rows = list(map(int, input.split("\n")))
	rows = input.split("\n")
	acc = 0
	index = 0
	visited = set()

	while not index in visited:
		visited.add(index)

		command, value = rows[index].split(" ")

		if command == "nop":
			index += 1
		elif command == "jmp":
			index += int(value)
		elif command == "acc":
			acc += int(value)
			index +=1
		
		if index >= len(rows):
			return True, acc

	return False, acc

def compute_part_2(input: str) -> int:
	base_rows = input.split("\n")

	for corrupted_index in range(0, len(base_rows)):
		rows = copy(base_rows)
		row = rows[corrupted_index]
		
		if row.startswith("jmp"):
			rows[corrupted_index] = row.replace("jmp", "nop")
		elif row.startswith("nop"):
			rows[corrupted_index] = row.replace("nop", "jmp")
		else:
			continue

		passed, acc = compute_part_1("\n".join(rows))

		if passed:
			return acc
	
	raise Exception()

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
