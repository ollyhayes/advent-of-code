input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0"
# input = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0"
test_input = "1,9,10,3,2,3,11,0,99,30,40,50"
# input = "1,0,0,0,99"
# input = "2,3,0,3,99"
# input = "2,4,4,5,99,0"
# input = "1,1,1,4,99,5,6,0,99"

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

def run_program(input: str, noun: int, verb: int):
	program = list(map(int, input.split(",")))
	program[1] = noun
	program[2] = verb
	index = 0
	while index < len(program):
		op_code = program[index]
		# print(f"i: {index}, op_code: {op_code}, program: {program[:10]}")
		operation = ops[op_code]
		index, program = operation(index, program)

	print(f"noun: {noun}, verb: {verb}, program: {program[:10]}")
	return program[0]

def search_for_value(input, value):
	for noun in range(0, 100):
		for verb in range(0, 100):
			output = run_program(input, noun, verb)

			if output == value:
				print(f"n: {noun}, v: {verb}")
				return noun, value


# test_output = run_program(test_input)
# assert test_output == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

# output = run_program(input, 12, 2)
# print(output)


# values = search_for_value(input, 4330636)
values = search_for_value(input, 19690720)
print(values)