import pytest

from day1 import compute_part_1, compute_part_2

@pytest.mark.parametrize(
	("input", "expected"),
	(
		("+1, -2, +3, +1", 3),
		("+1, +1, +1", 3),
		("+1, +1, -2", 0),
		("-1, -2, -3", -6),
	)
)
def test_part_1(input: str, expected: int) -> None:
	assert compute_part_1(input.replace(", ", "\n")) == expected

@pytest.mark.parametrize(
	("input", "expected"),
	(
		("+1, -2, +3, +1", 2),
		("+3, +3, +4, -2, -4", 10),
		("-6, +3, +8, +5, -6", 5),
		("+7, +7, -2, -7, -4", 14),
	)
)
def test_part_2(input: str, expected: int) -> None:
	assert compute_part_2(input.replace(", ", "\n")) == expected