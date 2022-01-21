result = 0
for i in range(2, 200000):
    digits = list(map(int, str(i)))
    fifth = 0

    for d in digits:
        fifth += d**5

    if i == fifth:
        result += i

print(result)
