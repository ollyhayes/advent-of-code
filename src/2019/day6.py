import os
from typing import List, Tuple, Dict, Set, Callable, Optional, Union, Set
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

def compute_part_1(input: str) -> int:
	orbits = list(input.split("\n"))
	planets = parse_orbits(orbits)
	orbit_count = 0

	for planet in planets.values():
		orbit_count += count_orbits(planet)

	return orbit_count

def compute_part_2(input: str) -> int:
	return 1

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day6_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	# print(f"part2: {compute_part_2(input)}")

	return 0

if __name__ == '__main__':
	exit(main())