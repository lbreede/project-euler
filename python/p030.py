#
# Solution to Project Euler Problem 30
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

result = 0
for i in range(2, 200000):
	digits = list(map(int, str(i)))
	fifth = 0

	for d in digits:
		fifth += d**5

	if i == fifth:
		result += i

print(result)