from math import sqrt

for a in range(1, 1000):
    for b in range(1, 1000):
        c = sqrt(a * a + b * b)
        if a + b + c == 1000:
            print(f"{a} * {b} * {c} = {a*b*c}")
            break
