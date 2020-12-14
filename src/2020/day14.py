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

def generate_float_masks(x_mask: str, on_mask) -> List[int]:
	# "00000XX0000000000X0X0000000000000X00"
	indices = []

	for index, character in enumerate(reversed(x_mask)):
		if character == "X":
			indices.append(index)

	permetations = pow(2, len(indices))
	masks = []

	for i in range(0, permetations):
		configuration = f"{i:b}"
		mask = on_mask

		for index, bit in enumerate(reversed(configuration)):
			if bit == "1":
				mask |= 1 << indices[index]

		print(f"{mask:b}")
		masks.append(mask)

	return masks


def compute_part_2(input: str) -> int:
	rows = input.split("\n")
	# on_mask = 0
	float_masks = []
	values: Dict[int, int] = {}

	for row in rows:
		field, value = row.split(" = ")
		if field == "mask":
			on_mask = int(value.replace("X", "0"), 2)
			float_masks = generate_float_masks(value.replace("1", "0"), on_mask)
		else:
			address = int(field.replace('mem[', '').replace(']', ''))

			for float_mask in float_masks:
				masked_address = address | float_mask
				values[masked_address] = int(value)


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
