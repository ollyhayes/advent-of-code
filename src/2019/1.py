from math import floor
from typing import List

input = """115919
56833
117651
56733
89472
91010
119618
85667
141042
106401
121495
50136
83755
122558
149188
110381
132060
145791
141381
136467
104712
133530
65297
52640
59637
78410
107791
96909
136738
109794
66831
58426
97955
90496
119294
83101
80466
114370
67631
106482
73996
50367
113976
68998
109714
96308
89350
143077
102052
93325
86870
94449
119448
53472
140668
64989
112056
88880
131335
94943
88061
122883
129059
55345
82362
60500
147652
83147
87106
97384
136883
62198
130290
129715
93082
72179
72109
70604
94894
98139
97056
86236
144191
108008
79225
93551
103116
130702
87599
143630
104476
108922
134209
85636
81591
127980
90425
126133
118135
93722"""
# input = "1969"

def fuel_required(mass):
	# print(mass)
	return max(floor(float(mass) / 3.0) - 2, 0)

def fuel_for_module(mass):
	fuel = fuel_required(mass)
	# print(f"mass: {mass}, fuel: {fuel}")
	fuel_for_fuel = fuel_required(fuel)

	if fuel_for_fuel > 0:
		return fuel + fuel_for_fuel + fuel_for_module(fuel_for_fuel)
	else:
		return fuel

def fuel_for_all_modules(module_masses: List[str]) -> str:
	total = 0
		
	for mass in module_masses:
		fuel = fuel_for_module(mass)
		# print(f"mass: {mass}, fuel: {fuel}")
		total += fuel

	return total


# print(fuel_for_all_modules(["14", "14"]))
# print(fuel_for_all_modules(["1969"]))
# print(fuel_for_all_modules(["100756"]))
# print(fuel_for_all_modules(["12"]))
# print(fuel_for_all_modules(["14"]))
# print(fuel_for_all_modules(["1969"]))
# print(fuel_for_all_modules(["100756"]))
print(fuel_for_all_modules(input.split("\n")))