from utils.math_functions import is_prime

i = 2
primes_found = 0
while True:
    if is_prime(i):
        primes_found += 1
        if primes_found == 10001:
            result = i
            break
    i += 1

print("Project Euler - 10001st Prime (Problem 7)")
print(f"Answer: {result:,}")
