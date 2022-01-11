from utils.math_functions import is_prime

result = 0
for x in range(2000000):
    if is_prime(x):
        result += x

print(result)