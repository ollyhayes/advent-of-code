from math import floor
from typing import List
import os
import pytest

def fuel_required(mass):
	# print(mass)
	return max(floor(float(mass) / 3.0) - 2, 0)

def fuel_for_module(mass):
	fuel = fuel_required(mass)
	if fuel > 0:
		return fuel + fuel_for_module(fuel)
	else:
		return fuel

def compute_part_1(input: str) -> int:
	module_masses = input.split("\n")
	total = 0
		
	for mass in module_masses:
		fuel = fuel_required(mass)
		# print(f"mass: {mass}, fuel: {fuel}")
		total += fuel

	return total

def compute_part_2(input: str) -> int:
	module_masses = input.split("\n")
	total = 0
		
	for mass in module_masses:
		fuel = fuel_for_module(mass)
		# print(f"mass: {mass}, fuel: {fuel}")
		total += fuel

	return total

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day1_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_2(input))

	return 0

if __name__ == '__main__':
	exit(main())

@pytest.mark.parametrize(
	("input", "expected"),
	(
		(12, 2),
		(14, 2),
		(1969, 654),
		(100756, 33583)
	)
)
def test_part_1(input, expected) -> None:
	assert compute_part_1(str(input)) == expected

@pytest.mark.parametrize(
	("input", "expected"),
	(
		(14, 2),
		(1969, 966),
		(100756, 50346)
	)
)
def test_part_2(input, expected) -> None:
	assert compute_part_2(str(input)) == expected