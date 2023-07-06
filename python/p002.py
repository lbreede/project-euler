a, b = 1, 2
result = 0

while b < 4_000_000:
    if b % 2 == 0:
        result += b
    c = a + b
    a = b
    b = c

print(result)
