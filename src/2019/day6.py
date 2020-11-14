import os
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Set, Generator
from itertools import zip_longest
from dataclasses import dataclass, field

@dataclass
class Planet():
	name: str
	orbits_planet: Optional["Planet"] = None
	outer_planets: List["Planet"] = field(default_factory=list)

def parse_orbits(orbits: List[str]) -> Dict[str, Planet]:
	planets: Dict[str, Planet] = {}

	def get_planet(name: str) -> Planet:
		if name in planets:
			return planets[name]

		planets[name] = new_planet = Planet(name=name)
		return new_planet

	for orbit in orbits:
		[inner, outer] = orbit.split(")")

		inner_planet = get_planet(inner)
		outer_planet = get_planet(outer)

		inner_planet.outer_planets.append(outer_planet)
		assert outer_planet.orbits_planet is None
		outer_planet.orbits_planet = inner_planet

	return planets

def count_orbits(planet: Planet) -> int:
	return 1 + count_orbits(planet.orbits_planet) if planet.orbits_planet else 0

def find_root(planet: Planet) -> Planet:
	return find_root(planet.orbits_planet) if planet.orbits_planet else planet

def draw_system(planets: List[Planet]) -> None:
	root = find_root(planets[0])
	output = [root.name]

	def inner(indent: str, planets: List[Planet]) -> None:
		for planet in planets:
			is_last = planet == planets[-1]

			output.append(indent + f"{'└' if is_last else '├'}─{planet.name}")

			path = " " if is_last else "│"

			inner(indent + path, planet.outer_planets)
		
	inner("", root.outer_planets)
	tree_drawing = "\n".join(output)

	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day6_output_tree.txt")
	with open(filename, "w") as output_file:
		output_file.write(tree_drawing)

def compute_part_1(input: str) -> int:
	orbits = list(input.split("\n"))
	planets = parse_orbits(orbits)
	orbit_count = 0

	for planet in planets.values():
		orbit_count += count_orbits(planet)

	return orbit_count

def compute_part_2(input: str) -> int:
	orbits = list(input.split("\n"))
	planets = parse_orbits(orbits)

	def get_path_to_sun(planet: Planet) -> Generator:
		distance = 1
		while planet.orbits_planet:
			planet = planet.orbits_planet
			yield planet.name, (planet, distance)
			distance += 1

	santa_orbiting = planets["SAN"].orbits_planet
	assert santa_orbiting
	santa_to_sun = dict(get_path_to_sun(santa_orbiting))

	you_orbiting = planets["YOU"].orbits_planet
	assert you_orbiting
	you_to_sun = dict(get_path_to_sun(you_orbiting))

	intersection_keys = santa_to_sun.keys() & you_to_sun.keys()
	distances = [
		santa_to_sun[intersection_point][1] + you_to_sun[intersection_point][1]
		for intersection_point
		in intersection_keys
	]

	return min(distances)

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day6_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	# orbits = list(input.split("\n"))
	# planets = parse_orbits(orbits)
	# draw_system(list(planets.values()))
	print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())