import pytest

from day1 import compute_part_1, compute_part_2

@pytest.mark.parametrize(
	("input", "expected"),
	(
		("6", 6),
		("159", 159),
		("135", 135),
	)
)
def test_part_1(input: str, expected: int) -> None:
	assert compute_part_1(input) == expected

# @pytest.mark.parametrize(
# 	("input", "expected"),
# 	(
# 		("input", 30),
# 		("input", 610),
# 		("input", 410),
# 	)
# )
# def test_part_2(input: str, expected: int) -> None:
# 	assert compute_part_2(input) == expected