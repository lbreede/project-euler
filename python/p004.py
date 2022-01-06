#
# Solution to Project Euler Problem 4
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

def main():
    start = 1000
    i = 0

    largestPalindrome = 0

    for x in range(1, start):
        for y in range(1, start):
            a = start - x
            b = start - y

            c = a * b

            if len(str(c)) % 2 == 0:
                front, back = splitEvenString(str(c))
                if mirrorAndCompare(front, back):
                    if c > largestPalindrome:
                        largestPalindrome = c
    
    print(largestPalindrome)

def splitEvenString(string):
    length = len(string)

    if length % 2 != 0:
        raise ValueError("Uneven amount of letters!")

    front = string[:length//2]
    back = string[length//2:]
    return front, back

def mirrorAndCompare(front, back):
    if int(front) == int(back[::-1]):
        return True
    else:
        return False
            
if __name__ == "__main__":
    main()