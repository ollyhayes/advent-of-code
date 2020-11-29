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
	relative_base: int

async def op_add(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	value = left.value + right.value
	assert output.write
	output.write(value)

async def op_multiply(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	value = left.value * right.value
	assert output.write
	output.write(value)

async def op_read(index: int, program_info: ProgramInfo, position: Parameter):
	input = await program_info.input.read()
	print(f"{program_info.instance_name}: <-- {input}")
	assert position.write
	position.write(input)

async def op_write(index: int, program_info: ProgramInfo, output: Parameter):
	print(f"{program_info.instance_name}: --> {output.value}")
	await program_info.output.write(output.value)

async def op_set_if(index, program_info: ProgramInfo, if_value: Parameter, new_index: Parameter):
	if if_value.value:
		return new_index.value

async def op_set_if_not(index, program_info: ProgramInfo, if_not_value: Parameter, new_index: Parameter):
	if not if_not_value.value:
		return new_index.value

async def op_leq(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value < right.value:
		output.write(1)
	else:
		output.write(0)

async def op_eq(index, program_info: ProgramInfo, left: Parameter, right: Parameter, output: Parameter):
	assert output.write
	if left.value == right.value:
		output.write(1)
	else:
		output.write(0)

async def op_set_base(index, program_info: ProgramInfo, new_base: Parameter):
	program_info.relative_base = new_base.value

async def op_terminate(index, program_info: ProgramInfo):
	print(f"{program_info.instance_name}: terminating")
	return len(program_info.program)

ops: Dict[int, Tuple[int, Callable]] = {
	1: (3, op_add),
	2: (3, op_multiply),
	3: (1, op_read),
	4: (1, op_write),
	5: (2, op_set_if),
	6: (2, op_set_if_not),
	7: (3, op_leq),
	8: (3, op_eq),
	9: (1, op_set_base),
	99: (0, op_terminate)
}

async def run_program(program: List[int], instance_name: str, input: Stream, output: Stream) -> List[int]:
	index = 0
	program_info = ProgramInfo(program, input, output, instance_name, 0)
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
			if parameter_type == "1": # immediate mode
				parameters.append(Parameter(value, None, None))
			else: # position/relative mode
				position = value + program_info.relative_base if parameter_type == "2" else value
				parameters.append(Parameter(program[position], position, lambda value_to_write: write(position, value_to_write)))

		print(f"{instance_name}: i: {index}, program: {program[index:index+10]}..., parameters: {[(parameter.value, parameter.position) for parameter in parameters]}")
		index = await operation(
			index,
			program_info,
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

	return output

def compute_part_2(input: str) -> int:
	output = 0
	
	return output

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day9_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	# print(f"total maximum: {compute_part_1(input)}")
	print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())
