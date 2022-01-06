#
# Solution to Project Euler Problem 48
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

def self_powers(start, end):
	a = 0
	for i in range(start, end+1):
		a += i**i
	return a

result = self_powers(1, 1000)
result = str(result)[-10:]
print(result)