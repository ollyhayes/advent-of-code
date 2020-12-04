from math import floor
from typing import List, Tuple
import os
import re

def compute_part_1(input: str) -> int:
	# lines = list(map(int, input.split("\n")))
	input_split = input.split("\n\n")

	passports = [{field.split(":")[0]: field.split(":")[1] for field in passport.replace("\n", " ").split(" ")} for passport in input_split]

	hair = re.compile('^#[0-9a-f]{6}$')
	eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
	pid = re.compile('^[0-9]{9}$')

	required_fields = {
		"byr": lambda value: 1920 <= int(value) <= 2002, # (Birth Year)
		"iyr": lambda value: 2010 <= int(value) <= 2020, # (Issue Year)
		"eyr": lambda value: 2020 <= int(value) <= 2030, # (Expiration Year)
		"hgt": lambda value: value[-2:] in {"cm", "in"} and (150 <= int(value[:-2]) <= 193) if value[-2:] == "cm" else (59 <= int(value[:-2]) <= 76), # (Height)
		"hcl": lambda value: hair.match(value), # (Hair Colour)
		"ecl": lambda value: value in eye_colours , # (Eye Colour)
		"pid": lambda value: pid.match(value), # (Passport ID)
		#  "cid" # (Country ID)
	}

	valid_passports = []
	for passport in passports:

		is_valid = required_fields.keys() <= passport.keys()

		if not is_valid:
			continue

		for key, validator in required_fields.items():
			try:
				if not validator(passport[key]):
					is_valid = False
			except:
				is_valid = False

		if is_valid:
			valid_passports.append(passport)
		

	return len(valid_passports)

def test():
	hair = re.compile('#[0-9a-f]{6}')
	eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
	pid = re.compile('[0-9]{9}')

	required_fields = {
		"byr": lambda value: 1920 <= int(value) <= 2002, # (Birth Year)
		"iyr": lambda value: 2010 <= int(value) <= 2020, # (Issue Year)
		"eyr": lambda value: 2020 <= int(value) <= 2030, # (Expiration Year)
		"hgt": lambda value: value[-2:] in {"cm", "in"} and (150 <= int(value[:-2]) <= 193) if value[-2:] == "cm" else (59 <= int(value[:-2]) <= 76), # (Height)
		"hcl": lambda value: len(hair) == 7 and hair.match(value), # (Hair Colour)
		"ecl": lambda value: value in eye_colours , # (Eye Colour)
		"pid": lambda value: len(value) == 9 and pid.match(value), # (Passport ID)
		#  "cid" # (Country ID)
	}

	assert required_fields['byr']("2002")
	assert not required_fields['byr']("2003")

	assert required_fields['hgt']("60in")
	assert required_fields['hgt']("190cm")
	assert not required_fields['hgt']("190in")
	assert not required_fields['hgt']("190")

	assert required_fields['hcl']("#123abc")
	assert not required_fields['hcl']("#123abz")
	assert not required_fields['hcl']("123abc")

	assert required_fields['ecl']("brn")
	assert not required_fields['ecl']("wat")

	assert required_fields['pid']("000000001")
	assert not required_fields['pid']("0123456789")

def main() -> int:
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, "day4_input.txt")
	with open(filename, "r") as input_file:
		input = input_file.read()

	print(compute_part_1(input))
	# test()

	return 0

if __name__ == '__main__':
	exit(main())
