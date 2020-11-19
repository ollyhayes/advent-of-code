import os
from typing import List, Tuple, Dict, Set, Callable, Optional, Union
from dataclasses import dataclass

@dataclass
class Layer:
	layer: List[int]
	digit_counts: List[int]


def compute_part_1(input: str) -> int:
	width = 25
	height = 6
	position = 0
	layers: List[Layer] = []

	layer_with_fewest_zeros: Optional[Layer] = None

	while position < len(input):
		current_layer_index = len(layers)
		layers.append(Layer([], [0, 0, 0]))
		current_layer = layers[current_layer_index]

		for x in range(0, width):
			for y in range(0, height):
				value = int(input[position])
				current_layer.layer.append(value)
				current_layer.digit_counts[value] += 1

				position += 1
		
		if not layer_with_fewest_zeros or layer_with_fewest_zeros.digit_counts[0] > current_layer.digit_counts[0]:
			layer_with_fewest_zeros = current_layer
	
	assert layer_with_fewest_zeros
	print(layer_with_fewest_zeros)

	print(layer_with_fewest_zeros.digit_counts[1] * layer_with_fewest_zeros.digit_counts[2])

	return 0

def compute_part_2(input: str) -> int:
	width = 25
	height = 6
	position = 0
	layers: List[Layer] = []

	while position < len(input):
		current_layer_index = len(layers)
		layers.append(Layer([], [0, 0, 0]))
		current_layer = layers[current_layer_index]

		for x in range(0, width):
			for y in range(0, height):
				value = int(input[position])
				current_layer.layer.append(value)
				current_layer.digit_counts[value] += 1

				position += 1
	
	# final_image = []
	position = 0
	print()
	
	for y in range(0, height):
		print(" ", end="")

		for x in range(0, width):
			def get_pixel(layer):
				value = layers[layer].layer[position]
				if value == 2:
					return get_pixel(layer + 1)
				elif value == 1:
					return "█"
				else:
					return " "

			value = get_pixel(0)
			print(value, end="")
			position += 1

		print()

	print()


def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day8_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	compute_part_1(input)
	compute_part_2(input)

	return 0

if __name__ == '__main__':
	exit(main())
