import os
from copy import copy
import sys, tty, termios
import asyncio
from asyncio import Queue, gather
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Protocol
from itertools import zip_longest
from dataclasses import dataclass, field

async def compute_part_1(input: str) -> Tuple[Tuple[int, int], int]:
	pass

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day10_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	compute_part_1(input)

	return 0

if __name__ == '__main__':
	exit(main())
