from math import floor, prod
from typing import Dict, List, Tuple, Optional
import os

def compute_part_1(input: str) -> Tuple[int, int]:
	input_split = input.split("\n")
	earliest_leave = int(input_split[0])
	bus_ids = [int(bus_id) for bus_id in input_split[1].split(",") if not bus_id == "x"]

	min_wait = 9999999

	for bus_id in bus_ids:
		wait = bus_id - (earliest_leave % bus_id)

		if wait < min_wait:
			min_wait = wait
			best_bus = bus_id

	return min_wait, best_bus

def compute_part_2(input: str) -> int:
	input_split = input.split("\n")
	bus_ids = [(next_bus_offset, int(next_bus_id)) for next_bus_offset, next_bus_id in enumerate(input_split[1].split(",")) if next_bus_id != "x"]

	def find_next_pattern(start, x_multiplier, y_offset, y_multiplier):
		timestamp = start
		while True:
			if (timestamp + y_offset) % y_multiplier == 0:
				return timestamp, x_multiplier * y_multiplier
			
			timestamp += x_multiplier
	
	timestamp = 0
	multiplier = bus_ids[0][1]  # we can always multiply by this and keep the existing pattern

	for next_bus_offset, next_bus_id in bus_ids[1:]:
		timestamp, multiplier = find_next_pattern(timestamp, multiplier, next_bus_offset, next_bus_id)

	return timestamp

def main() -> int:
	input_filename = f"{__file__.split('.')[0]}_input.txt"
	with open(input_filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
