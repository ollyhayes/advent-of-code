import os
import sys, tty, termios
from typing import List, Tuple, Dict, Set, Callable, Optional, Union
from itertools import zip_longest
from dataclasses import dataclass

@dataclass
class Parameter():
	value: int
	position: Optional[int]
	write: Optional[Callable[[int], None]]

def op_1(index, program, left: Parameter, right: Parameter, output: Parameter):
	value = left.value + right.value
	assert output.write
	output.write(value)

def op_2(index, program, left: Parameter, right: Parameter, output: Parameter):
	value = left.value * right.value
	assert output.write
	output.write(value)

def op_3(index: int, program: List[int], position: Parameter):
	print(f"enter value")
	input = int(sys.stdin.read(1))
	print(f"received: {input}")
	assert position.write
	position.write(input)

def op_4(index: int, program: List[int], output: Parameter):
	print(f"output: {output.value}")

def op_5(index, program, if_value: Parameter, new_index: Parameter):
	if if_value.value:
		return new_index.value

def op_6(index, program, if_not_value: Parameter, new_index: Parameter):
	if not if_not_value.value:
		return new_index.value

def op_7(index, program, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value < right.value:
		output.write(1)
	else:
		output.write(0)

def op_8(index, program, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value == right.value:
		output.write(1)
	else:
		output.write(0)

def op_99(index, program):
	print(f"terminating")
	return len(program)

ops: Dict[int, Tuple[int, Callable]] = {
	1: (3, op_1),
	2: (3, op_2),
	3: (1, op_3),
	4: (1, op_4),
	5: (2, op_5),
	6: (2, op_6),
	7: (3, op_7),
	8: (3, op_8),
	99: (0, op_99)
}

def compute_part_1(input: str) -> List[int]:
	program = list(map(int, input.split(",")))
	index = 0
	while index < len(program):
		op_code_info = program[index]
		op_code = int(str(op_code_info)[-2:])
		param_info: Union[str, List] = str(op_code_info)[0:-2] or []

		parameter_count, operation = ops[op_code]

		parameter_values = [program[index + 1 + i] for i in range(0, parameter_count)]
		parameter_types = reversed(param_info)

		def write(position, value):
			program[position] = value

		parameters = []
		for value, parameter_type in zip_longest(parameter_values, parameter_types):
			if parameter_type == "1":
				parameters.append(Parameter(value, None, None))
			else:
				parameters.append(Parameter(program[value], value, lambda value_to_write: write(value, value_to_write)))

		print(f"i: {index}, op_code: {op_code}, program: {program[index:index+10]}..., parameters: {[(parameter.value, parameter.position) for parameter in parameters]}")
		index = operation(index, program, *parameters) or index + 1 + parameter_count

	return program

def compute_part_2(input: str) -> int:
	return 1

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day5_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	compute_part_1(input)
	# print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	fd = sys.stdin.fileno()
	old = termios.tcgetattr(fd)
	tty.setcbreak(fd)

	try:
		main()
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old)

	exit(0)

	# while True:
	# 	line = sys.stdin.read(1)
	# 	print(f'Processsssing Message from sys.stdin *****{line}*****')

	# 	if line == "q":
	# 		print('exiting')
	# 		break

	# tty.setraw(stdin_fd)
