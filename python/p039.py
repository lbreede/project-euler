#
# Solution to Project Euler Problem 39
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

# Integer right triangles

from math import sqrt

a = 20
b = 48
c = 52

# print (120 == a + b + sqrt(a*a + b*b))

number = 0
most_solutions = 0

for i in range(1,1001):
	solutions = 0
	for a in range(1, i+1):
		for b in range(a, i+1):
			if a + b + sqrt(a*a + b*b) == i:
				solutions += 1

	if solutions > most_solutions:
		most_solutions = solutions
		number = i

print(number, most_solutions)
