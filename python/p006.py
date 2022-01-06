#
# Solution to Project Euler Problem 6
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

def main():
	max_ = 100

	return squareOfSum(max_) - sumOfSquares(max_)

def sumOfSquares(max_):
	result = 0
	for x in range(1, max_+1):
		result += x * x

	return result

def squareOfSum(max_):
	result = 0
	for x in range(1, max_+1):
		result += x

	return result * result

if __name__ == "__main__":
	print(main())