def findMultiples(inputdata):
    multiples = []
    for x in range(1, inputdata):
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)

    return sum(multiples)

sumOfMultiples = findMultiples(1000)
print(sumOfMultiples)