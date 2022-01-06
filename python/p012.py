#
# Solution to Project Euler Problem 12
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

def triangle(n):
	t = 0
	for i in range(n):
		t += i+1
	return t

i = 1
while True:
	t = triangle(i)
	divs = 0
	for j in range(1, t+1):
		if t % j == 0:
			divs += 1
	print(f"Number: {i}, Triangle Number: {t}, Divisors: {divs}")
	if divs > 500:		
		break
	i += 1