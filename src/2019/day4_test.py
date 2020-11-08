import pytest
from day4 import is_valid

@pytest.mark.parametrize(
	("input", "expected"),
	(
		(111111, False),
		(223450, False),
		(123789, False),
		(112233, True),
		(123444, False),
		(111122, True),
	)
)
def test_part_1(input: int, expected: bool) -> None:
	assert is_valid(input) == expected
