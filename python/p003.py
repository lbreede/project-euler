#
# Solution to Project Euler Problem 3
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

start = 600851475143.0
divisor = 2

primes = 0

while True:
    temp_start = start / divisor
    if temp_start % 1 == 0:
        if divisor > primes:
            primes = divisor
        start = temp_start
        if start == 1:
            break
    else:
        divisor += 1

print(primes)
