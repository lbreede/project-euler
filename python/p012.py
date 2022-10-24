# Highly divisible triangular number

"""
Problem 12
    The sequence of triangle numbers is generated by adding the natural
    numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    The first ten terms would be:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred
    divisors?

"""


def triangle(n):
    # tn = ½n(n+1)
    return int(0.5 * n * n + 0.5 * n)


i = 0
ndivs = 0
while ndivs <= 500:
    i += 1
    tn = triangle(i)
    ndivs = 0
    for j in range(1, tn + 1):
        if tn % j == 0:
            ndivs += 1
    print(i, tn, ndivs)


print(tn)
