#
# Solution to Project Euler Problem 10
# Copyright (c) Lennart Breede. All rights reserved.
# https://github.com/lbreede/project-euler
#

from utils import math_functions as mf

result = 0
for x in range(2000000):
    if mf.is_prime(x):
        result += x

print(result)