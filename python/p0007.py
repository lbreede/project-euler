from utils import math_functions as mf

i = 2

primes_found = 0

while True:
    if mf.is_prime(i):
        primes_found += 1
        if primes_found == 10001:
            result = i
            break
    i += 1

print(result)