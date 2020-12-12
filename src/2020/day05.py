from math import floor
from typing import DefaultDict, Dict, List, Tuple
import os

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	lines = input.split("\n")
	max_seat_id = 0

	seats = DefaultDict(lambda: DefaultDict(lambda: " "))

	for line in lines:
		row_specifier = line[:7].replace("F", "0").replace("B", "1")
		column_specifier = line[7:].replace("L", "0").replace("R", "1")

		row = int(row_specifier, 2)
		column = int(column_specifier, 2)

		seats[row][column] = "x"

		seat_id = row * 8 + column

		max_seat_id = max(seat_id, max_seat_id)

	print_seats(seats)

	return max_seat_id

def print_seats(seats: dict):
	for key, row in sorted(seats.items(), key=lambda kv: kv[0]):
		row_sorted = sorted(row.items(), key=lambda kv: kv[0])

		print(f"key: {key}, " + "".join(row for key, row in row_sorted))


def compute_part_2(input: str) -> int:
	return 0

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day05_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
