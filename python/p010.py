from utils import math_functions as mf

result = 0
for x in range(2000000):
    if mf.is_prime(x):
        result += x

print(result)