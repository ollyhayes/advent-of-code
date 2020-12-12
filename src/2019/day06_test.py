import os
import pytest
from day06 import compute_part_2

def test_part_1() -> None:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day06_input_test.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	assert compute_part_2(input) == 4
