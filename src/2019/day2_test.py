import pytest
from typing import List
from day2 import compute_part_1

@pytest.mark.parametrize(
	("input", "expected"),
	(
		("1,0,0,0,99", [2,0,0,0,99]),
		("2,3,0,3,99", [2,3,0,6,99]),
		("2,4,4,5,99,0", [2,4,4,5,99,9801]),
		("1,1,1,4,99,5,6,0,99", [30,1,1,4,2,5,6,0,99])
	)
)
def test_part_1(input: str, expected: List[int]) -> None:
	assert compute_part_1(input) == expected