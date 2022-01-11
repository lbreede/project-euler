a = 1
b = 2

result = 0

while b < 4000000:
    if b % 2 == 0:
        result += b
    c = a + b
    a = b
    b = c
    
print(result)