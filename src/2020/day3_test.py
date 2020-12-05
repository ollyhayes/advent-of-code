import os
import pytest
from day3 import compute_part_1, compute_part_2
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Protocol

t1 = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""", (3, 1), 7


@pytest.mark.parametrize(
	("field", "direction", "trees"),
	(t1, t1)
)
def test_part_1(field: str, direction: Tuple[int, int], trees: int) -> None:
	assert compute_part_1(field, direction) == trees