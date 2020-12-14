from math import floor
from typing import Dict, List, Tuple, Optional
import os
import re

def compute_part_1(input: str) -> int:
	rows = input.split("\n")
	on_mask = 0
	off_mask = pow(2, 36) - 1
	values: Dict[int, int] = {}

	for row in rows:
		field, value = row.split(" = ")
		if field == "mask":
			on_mask = int(value.replace("X", "0"), 2)
			off_mask = int(value.replace("X", "1"), 2)
		else:
			address = int(field.replace('mem[', '').replace(']', ''))
			masked_value = (int(value) | on_mask) & off_mask
			values[address] = masked_value

	return sum(values.values())

def apply_x_masks(x_mask: str, initial_value: int) -> List[int]:
	x_indices = []

	for index, character in enumerate(reversed(x_mask)):
		if character == "X":
			x_indices.append(index)

	number_of_permutations = pow(2, len(x_indices))
	outputs = []

	for i in range(0, number_of_permutations):
		permutation = f"{i:b}".zfill(len(x_indices))
		value = initial_value

		for index, bit in enumerate(reversed(permutation)):
			if bit == "1":
				value |= 1 << x_indices[index]
			elif bit == "0":
				value &= ~(1 << x_indices[index])

		# print(f"{mask:036b}")
		outputs.append(value)

	return outputs


def compute_part_2(input: str) -> int:
	rows = input.split("\n")
	values: Dict[int, int] = {}
	on_mask = 0
	x_mask = ''

	for row in rows:
		field, value = row.split(" = ")
		if field == "mask":
			on_mask = int(value.replace("X", "0"), 2)
			x_mask = value.replace("1", "0")
		else:
			address = int(field.replace('mem[', '').replace(']', ''))

			for address in apply_x_masks(x_mask, address | on_mask):
				values[address] = int(value)

	return sum(values.values())

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
