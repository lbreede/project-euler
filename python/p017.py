#
# Solution to Project Euler Problem 17
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

from math import floor

conversion = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
	7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
	13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
	17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
	40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
	90: "ninety"}


def main():
	
	super_word = ""

	for x in range(1, 1001):
		super_word += numToWord(x)

	print(len(super_word.replace(" ", "")))

def numToWord(num):
	if num >= 1 and num <= 19:
		return conversion[num]
	elif num >= 20 and num <= 99:
		return convertTens(num)
	elif num >= 100 and num <= 999:
		return convertHundreds(num)
	elif num == 1000:
		return "one thousand"

def convertTens(num):
	remainder = num % 10
	if remainder == 0:
		return conversion[num]
	else:
		return f"{conversion[num - remainder]} {conversion[remainder]}"

def convertHundreds(num):
	word = ""
	base = floor(num * 0.01)
	word += conversion[base] + " hundred"
	rest = num - base * 100
	if rest >= 1 and rest <= 19:
		word += " and "
		word += conversion[rest]
	elif rest >= 20 and rest <= 99:
		word += " and "
		word += convertTens(rest)

	return word

	




if __name__ == '__main__':
	main()
	# convertHundrets(301)

