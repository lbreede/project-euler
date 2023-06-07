# Circular primes

"""
Problem 35

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
"""

from utils.math_functions import is_prime


def is_circular_prime(num):
    num = str(num)
    for i, x in enumerate(num):
        if not is_prime(int(num[i:] + num[:i])):
            return False
    return True


def main():
    mx = 1000000
    circular_primes = set()
    for i in range(1, mx):
        if is_circular_prime(i):
            circular_primes.add(i)

    print(len(circular_primes))


if __name__ == "__main__":
    main()
