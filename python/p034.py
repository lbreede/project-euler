#
# Solution to Project Euler Problem 34
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

# Digit factorials

from math import factorial

nums = set()
for i in range(3, 1500000):
	s = 0
	for j in str(i):
		s += factorial(int(j))
	if i == s:
		nums.add(i)
print(sum(nums))