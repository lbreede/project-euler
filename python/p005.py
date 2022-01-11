smallestEvenlyDivisible = 20.0
max_value = 20

while True:
    
    success = 0
    for x in range(1, max_value+1):
        if smallestEvenlyDivisible / x % 1 == 0:
            success += 1
    
    if success == max_value:
        break
    else:
        smallestEvenlyDivisible += max_value

print(smallestEvenlyDivisible)