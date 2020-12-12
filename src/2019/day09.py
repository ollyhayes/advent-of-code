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

	async def write(self, value: int) -> None:
		if self.pipe_to:
			await self.pipe_to.write(value)
		else:
			await self.queue.put(value)

	def pipe(self, stream: "Stream") -> None:
		self.pipe_to = stream

	async def read(self) -> int:
		value = await self.queue.get()
		# print(f"reading: {value}, queue: {self.queue}")
		return value

# @dataclass
# class StdIn():
# 	async def read(self) -> int:
# 		input = await int(sys.stdin.read(1))

@dataclass
class StdOut(Stream):
	async def write(self, value: int) -> None:
		pass

# def input_from_stdin() -> int:
# 	print(f"enter value")
# 	input = int(sys.stdin.read(1))
# 	print(f"received: {input}")
# 	return input

# def output_to_stdin(output: int) -> None:
# 	print(f"output: {output}")

@dataclass
class ProgramInfo():
	program: Dict[int, int]
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
	program_info.relative_base += new_base.value

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

async def run_program(program: Dict[int, int], instance_name: str, input: Stream, output: Stream) -> Dict[int, int]:
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
				parameters.append(Parameter(program.get(position, 0), position, lambda value_to_write: write(position, value_to_write)))

		# print(f"i: {index},\tprogram: {program}..., parameters: {[(parameter.value, parameter.position) for parameter in parameters]}")
		print(f"{instance_name}: i: {index}, program: {print_range(index, program)}..., parameters: {[(parameter.value, parameter.position) for parameter in parameters]}")

		new_index = await operation(index, program_info, *parameters) 
		index = new_index if new_index is not None else index + 1 + parameter_count

	return program

def print_range(index: int, program: Dict[int, int]) -> str:
	return "[" + ",".join([str(program.get(index, "?")) for index in range(index, index + 10)]) + "]"

async def compute(input_program: str, input_code: int) -> None:
	program = {index: value for index, value in enumerate(map(int, input_program.split(",")))}
	# program = {index: value for index, value in enumerate([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])}
	# program = {index: value for index, value in enumerate([1102,34915192,34915192,7,4,7,99,0])}
	# program = {index: value for index, value in enumerate([104,1125899906842624,99])}

	input, output = Stream(), StdOut()

	await input.write(input_code)

	await run_program(program, "main", input, output)

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day09_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	asyncio.run(compute(input, 1))
	asyncio.run(compute(input, 2))

	return 0

if __name__ == '__main__':
	exit(main())
