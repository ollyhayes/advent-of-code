import os
import sys, tty, termios
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Protocol
from itertools import zip_longest
from dataclasses import dataclass, field

@dataclass
class Parameter():
	value: int
	position: Optional[int]
	write: Optional[Callable[[int], None]]

@dataclass
class Stream():
	buffer: List[int] = field(default_factory=list)

	def write(self, value: int) -> None:
		self.buffer.append(value)
		print(f"writing: {value}, buffer: {self.buffer}")

	# def pipe(self, stream: "Stream") -> None:
	# 	stream.buffer = self.buffer

	def read(self) -> int:
		value = self.buffer.pop(0)
		print(f"reading: {value}, buffer: {self.buffer}")
		return value

@dataclass
class ProgramInfo():
	program: List[int]
	input: Stream
	output: Stream

def op_1(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	value = left.value + right.value
	assert output.write
	output.write(value)

def op_2(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	value = left.value * right.value
	assert output.write
	output.write(value)

def op_3(index: int, program_info: ProgramInfo, position: Parameter):
	input = program_info.input.read()
	assert position.write
	position.write(input)

def op_4(index: int, program_info: ProgramInfo, output: Parameter):
	program_info.output.write(output.value)

def op_5(index, program_info: ProgramInfo, if_value: Parameter, new_index: Parameter):
	if if_value.value:
		return new_index.value

def op_6(index, program_info: ProgramInfo, if_not_value: Parameter, new_index: Parameter):
	if not if_not_value.value:
		return new_index.value

def op_7(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value < right.value:
		output.write(1)
	else:
		output.write(0)

def op_8(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value == right.value:
		output.write(1)
	else:
		output.write(0)

def op_99(index, program_info: ProgramInfo):
	print(f"terminating")
	return len(program_info.program)

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

def run_program(program: List[int], instance_name: str, input: Stream, output: Stream) -> List[int]:
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

		print(f"instance: {instance_name}, i: {index}, program: {program[index:index+10]}..., parameters: {[(parameter.value, parameter.position) for parameter in parameters]}")
		index = operation(index, ProgramInfo(program, input, output), *parameters) or index + 1 + parameter_count

	return program

# def input_from_stdin() -> int:
# 	print(f"enter value")
# 	input = int(sys.stdin.read(1))
# 	print(f"received: {input}")
# 	return input

# def output_to_stdin(output: int) -> None:
# 	print(f"output: {output}")

def compute_output_signal(input_program: str, sequence: List[int]) -> int:
	program = list(map(int, input_program.split(",")))

	current_signal = 0

	for i, phase in enumerate(sequence):
		input, output = Stream(), Stream()

		input.write(phase)
		input.write(current_signal)

		run_program(program, str(i), input, output)
		current_signal = output.read()
	
	return current_signal

def compute_part_1(input: str) -> None:
	print(compute_output_signal(input, [1, 2, 3, 4, 5]))

def compute_part_2(input: str) -> int:
	return 1

# def main() -> int:
# 	dirname = os.path.dirname(__file__)
# 	filename = os.path.join(dirname, "day5_input.txt")
# 	with open(filename, "r") as input_file:
# 		input = input_file.read()

# 	compute_part_1(input)
# 	# print(f"part2: {compute_part_2(input)}")

# 	return 0

# if __name__ == '__main__':
# 	fd = sys.stdin.fileno()
# 	old = termios.tcgetattr(fd)
# 	tty.setcbreak(fd)

# 	try:
# 		main()
# 	finally:
# 		termios.tcsetattr(fd, termios.TCSADRAIN, old)

# 	exit(0)

	# while True:
	# 	line = sys.stdin.read(1)
	# 	print(f'Processsssing Message from sys.stdin *****{line}*****')

	# 	if line == "q":
	# 		print('exiting')
	# 		break

	# tty.setraw(stdin_fd)
