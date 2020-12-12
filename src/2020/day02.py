from math import floor
from typing import List
import os
import re

regex = re.compile('(\d+)-(\d+) (\w): (\w+)')

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	lines = input.split("\n")

	valid = 0
	invalid = 0

	for line in lines:
		min, max, letter, password = regex.findall(line)[0]

		if int(min) <= password.count(letter)  <= int(max):
			valid += 1
		else:
			invalid += 1

	print(invalid)
	print(valid)
	return 0

def compute_part_2(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	lines = input.split("\n")

	valid = 0
	invalid = 0

	for line in lines:
		min, max, letter, password = regex.findall(line)[0]

		correct = 0
		if password[int(min) - 1] == letter:
			correct += 1
		if password[int(max) - 1] == letter:
			correct += 1

		if correct == 1:
			valid += 1
		else:
			invalid += 1

	print(invalid)
	print(valid)
	return 0

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day02_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())
