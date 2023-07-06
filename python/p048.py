def self_powers(start, end):
    a = 0
    for i in range(start, end + 1):
        a += i**i
    return a


result = self_powers(1, 1000)
result = str(result)[-10:]
print(result)
