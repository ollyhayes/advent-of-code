import os
from copy import copy
import sys, tty, termios
import asyncio
from asyncio import Queue, gather
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
	queue: Queue = field(default_factory=lambda: asyncio.Queue(1))
	pipe_to: Optional["Stream"] = None
	pipe_to_output: int = 0

	async def write(self, value: int) -> None:
		if self.pipe_to:
			await self.pipe_to.write(value)
			self.pipe_to_output = value
		else:
			await self.queue.put(value)

	def pipe(self, stream: "Stream") -> None:
		self.pipe_to = stream

	async def read(self) -> int:
		value = await self.queue.get()
		# print(f"reading: {value}, queue: {self.queue}")
		return value

@dataclass
class ProgramInfo():
	program: List[int]
	input: Stream
	output: Stream
	instance_name: str

async def op_1(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	value = left.value + right.value
	assert output.write
	output.write(value)

async def op_2(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	value = left.value * right.value
	assert output.write
	output.write(value)

async def op_3(index: int, program_info: ProgramInfo, position: Parameter):
	input = await program_info.input.read()
	print(f"{program_info.instance_name}: <-- {input}")
	assert position.write
	position.write(input)

async def op_4(index: int, program_info: ProgramInfo, output: Parameter):
	print(f"{program_info.instance_name}: --> {output.value}")
	await program_info.output.write(output.value)

async def op_5(index, program_info: ProgramInfo, if_value: Parameter, new_index: Parameter):
	if if_value.value:
		return new_index.value

async def op_6(index, program_info: ProgramInfo, if_not_value: Parameter, new_index: Parameter):
	if not if_not_value.value:
		return new_index.value

async def op_7(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value < right.value:
		output.write(1)
	else:
		output.write(0)

async def op_8(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value == right.value:
		output.write(1)
	else:
		output.write(0)

async def op_99(index, program_info: ProgramInfo):
	print(f"{program_info.instance_name}: terminating")
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

async def run_program(program: List[int], instance_name: str, input: Stream, output: Stream) -> List[int]:
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

		print(f"{instance_name}: i: {index}, program: {program[index:index+10]}..., parameters: {[(parameter.value, parameter.position) for parameter in parameters]}")
		index = await operation(
			index,
			ProgramInfo(program, input, output, instance_name),
			*parameters) or index + 1 + parameter_count

	return program

# def input_from_stdin() -> int:
# 	print(f"enter value")
# 	input = int(sys.stdin.read(1))
# 	print(f"received: {input}")
# 	return input

# def output_to_stdin(output: int) -> None:
# 	print(f"output: {output}")

async def compute_output_signal_part_1(input_program: str, sequence: List[int]) -> int:
	program = list(map(int, input_program.split(",")))

	current_signal = 0

	for i, phase in enumerate(sequence):
		input, output = Stream(), Stream()

		asyncio.create_task(run_program(program, str(i), input, output))

		await input.write(phase)
		await input.write(current_signal)

		current_signal = await output.read()
		
		print(f"completed iteration {i}, signal = {current_signal}")
		print()
	
	return current_signal

def compute_part_1(input: str) -> int:
	output = 0

	for i in range(0, 3125):
		phase_attempt = convert_to_base(i, 5)
		if len(set(phase_attempt)) == len(phase_attempt):
			new_output = asyncio.run(compute_output_signal_part_1(input, [int(char) for char in phase_attempt]))
			output = max(output, new_output)
	
	return output

def convert_to_base(input: int, base: int) -> str:
	value = ""
	while input:
		value = str(input % base) + value
		input //= 5

	return value.zfill(5)

async def compute_output_signal_part_2(input_program: str, sequence: List[int]) -> int:
	program = list(map(int, input_program.split(",")))

	thrusters = []
	initial_output = Stream()
	previous_output = initial_output

	for i, phase in enumerate(sequence):
		input, output = Stream(), Stream()

		thrusters.append(asyncio.create_task(run_program(copy(program), str(i), input, output)))

		await input.write(phase)
		previous_output.pipe(input)

		previous_output = output

	previous_output.pipe(initial_output)

	await initial_output.write(0)
	await gather(*thrusters)
	
	return previous_output.pipe_to_output

def compute_part_2(input: str) -> int:
	output = 0

	for i in range(0, 3125):
		phase_attempt = convert_to_base(i, 5)
		if len(set(phase_attempt)) == len(phase_attempt):
			new_output = asyncio.run(compute_output_signal_part_2(input, [int(char) + 5 for char in phase_attempt]))
			output = max(output, new_output)
	
	return output

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day07_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	# print(f"total maximum: {compute_part_1(input)}")
	print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())
