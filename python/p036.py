#
# Solution to Project Euler Problem 36
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

from math import floor

def is_palindrome(a):
	L = len(a)
	h = floor(L * 0.5)
	p1 = a[:h]
	if L % 2:
		h += 1
	p2 = a[h:][::-1]
	if p1 == p2: return True
	else:		 return False

result = 0
for i in range(1000001):
	d = str(i)
	b = bin(i)[2:]
	if is_palindrome(d) and is_palindrome(b):
		result += i

print(result)