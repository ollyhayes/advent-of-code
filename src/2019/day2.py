import os
from typing import List

def get_referenced_value(index, program):
	return program[program[index]]

def op_1(index, program):
	left = get_referenced_value(index + 1, program)
	right = get_referenced_value(index + 2, program)
	value = left + right
	pos = program[index + 3]

	# print(f"add: {left} + {right} = {value} @ {pos}")

	program[pos] = value

	return index + 4, program

def op_2(index, program):
	left = get_referenced_value(index + 1, program)
	right = get_referenced_value(index + 2, program)
	value = left * right
	pos = program[index + 3]

	# print(f"multiply: {left} + {right} = {value} @ {pos}")

	program[pos] = value

	return index + 4, program

def op_99(index, program):
	return len(program), program

ops = {
	1: op_1,
	2: op_2,
	99: op_99
}

def compute_part_1(input: str) -> List[int]:
	program = list(map(int, input.split(",")))
	index = 0
	while index < len(program):
		op_code = program[index]
		# print(f"i: {index}, op_code: {op_code}, program: {program[:10]}")
		operation = ops[op_code]
		index, program = operation(index, program)

	# print(f"noun: {noun}, verb: {verb}, program: {program[:10]}")
	return program

def run_program(input: str, noun: int, verb: int) -> int:
	program = list(map(int, input.split(",")))
	program[1] = noun
	program[2] = verb
	index = 0
	while index < len(program):
		op_code = program[index]
		# print(f"i: {index}, op_code: {op_code}, program: {program[:10]}")
		operation = ops[op_code]
		index, program = operation(index, program)

	# print(f"noun: {noun}, verb: {verb}, program: {program[:10]}")
	return program[0]

def compute_part_2(input, value):
	for noun in range(0, 100):
		for verb in range(0, 100):
			output = run_program(input, noun, verb)

			if output == value:
				# print(f"n: {noun}, v: {verb}")
				return noun, verb

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day2_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(f"part1: {compute_part_1(input)[0]}")
	print(f"part2: {compute_part_2(input, 19690720)}")

	return 0

if __name__ == '__main__':
	exit(main())