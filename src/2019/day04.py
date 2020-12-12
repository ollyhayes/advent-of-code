import os
from typing import List, Tuple, Dict, Set

def is_valid(input: int) -> bool:
	has_double = False

	for i in range(0, 5):
		prev = int(str(input)[i - 1]) if i > 0 else None
		left = int(str(input)[i])
		right = int(str(input)[i + 1])
		next = int(str(input)[i + 2]) if i < 4 else None

		if left > right:
			return False

		if left == right and left != prev and left != next:
			has_double = True

	return has_double

def compute_part_1() -> int:
	count = 0
	for i in range(254032, 789860):
		if is_valid(i):
			count += 1
	
	return count

def main() -> int:
	print(f"part1: {compute_part_1()}")

	return 0

if __name__ == '__main__':
	exit(main())