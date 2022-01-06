#
# Solution to Project Euler Problem 9
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

from math import sqrt

for a in range(1, 1000):
	for b in range(1, 1000):
		c = sqrt(a*a + b*b)
		if a+b+c == 1000:
			print(f"{a} * {b} * {c} = {a*b*c}")
			break
