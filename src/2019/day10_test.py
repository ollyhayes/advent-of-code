import os
import pytest
from day10 import compute_part_1
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Protocol

t1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""", (5,8), 33

t2 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""", (1,2), 35

t3 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""", (6,3), 41

t4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""", (11,13), 210

@pytest.mark.parametrize(
	("field", "best_position", "astroids_detected"),
	( t1, t2, t3, t4 )
)
def test_part_1(field: str, best_position: Tuple[int, int], astroids_detected: int) -> None:
	assert compute_part_1(field) == (best_position, astroids_detected)

# @pytest.mark.parametrize(
# 	("program", "sequence", "expected"),
# 	(
# 		("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5", [9,8,7,6,5], 139629729),
# 		("3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10", [9,7,8,5,6], 18216),
# 	)
# )
# @pytest.mark.asyncio
# async def test_part_2(program: str, sequence: List[int], expected: List[int]) -> None:
# 	assert await compute_part_1(program, sequence) == expected