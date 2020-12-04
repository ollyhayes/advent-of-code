from math import floor
from typing import List, Tuple
import os

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	input_split = input.split("\n\n")

	# fields = [field.split(":") for field in passport.replace("\n", " ").split(" ") for passport in passports]

	passports = [{field.split(":")[0]: field.split(":")[1] for field in passport.replace("\n", " ").split(" ")} for passport in input_split]

	required_fields = {
    "byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Colour)
    "ecl", # (Eye Colour)
    "pid", # (Passport ID)
   #  "cid" # (Country ID)
	}

	invalid_passports = []
	for passport in passports:
		if not required_fields <= passport.keys():
			invalid_passports.append(passport)

	return len(invalid_passports)

def add(x, y, width):
	return (x[0] + y[0]) % width, x[1] + y[1]

# def compute_part_2(input: str) -> int:
# 	slopes = [
# 		(1, 1),
# 		(3, 1),
# 		(5, 1),
# 		(7, 1),
# 		(1, 2),
# 	]
# 	total_trees_multiplied = 1

# 	for slope in slopes:
# 		trees = compute_part_1(input, slope)
# 		total_trees_multiplied *= trees

# 	return total_trees_multiplied

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day4_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	# print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
