#!/usr/bin/python
import click
import shutil
import os

# DAY_NUMBER=$1
# YEAR_NUMBER=2020
# DIR="$(dirname "${BASH_SOURCE[0]}")"
# DIR="$(realpath "${DIR}")"   

# echo $DIR"/"$YEAR_NUMBER"/"

# 	input_filename = f"{__file__.split('.')[0]}_input.txt"

# cp template /

@click.command()
@click.argument('day', required=True, type=int)
@click.argument('year', default=2020, type=int)
def main(day: int, year: int) -> int:
	assert 0 <= day <= 25
	assert 2015 <= year <= 2020

	src_dir = os.path.dirname(__file__)
	template = os.path.join(src_dir, "template.py")
	script_file = os.path.join(src_dir, str(year), f"day{day}.py")
	input_file = os.path.join(src_dir, str(year), f"day{day}_input.txt")

	shutil.copyfile(template, script_file)

	os.system(f"curl -o {input_file} -H 'Cookie: session={os.environ['ADVENT_SESSION']}' https://adventofcode.com/{year}/day/{day}/input")

	return 0

if __name__ == '__main__':
	exit(main())
