def find_multiples(inputdata):
    multiples = []
    for x in range(1, inputdata):
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)

    return sum(multiples)

sum_of_multiples = find_multiples(1000)
print(sum_of_multiples)