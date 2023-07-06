start = 600_851_475_143.0
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
