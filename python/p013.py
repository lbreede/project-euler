#
# Solution to Project Euler Problem 13
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

with open("p013_numbers.txt", "r") as f:
	numbers = list(map(int, f.read().split("\n")))
	
result = str(sum(numbers))[:10]
print(result)