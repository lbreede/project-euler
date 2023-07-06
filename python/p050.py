from utils.math_functions import is_prime

primes = []
prime = 0
lst = []
i = 0
while True:
    if is_prime(i):
        primes.append(i)
        s = sum(primes)

        if is_prime(s):
            prime = s
            if prime < 1000:
                lst.append([prime, len(primes)])
            else:
                break

    i += 1

print(lst)

# doesn't necessarily start at 2!!!
a = 21
b = 3
print(sum(primes[b : a + b]), len(primes[b : a + b]), primes[b : a + b])
