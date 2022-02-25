# Factorial digit sum


def fac(n):
    f = 1
    for i in range(n):
        f *= n - i
    return f


def fac_digit_sum(n):
    f = str(fac(n))
    sum_ = 0
    for digit in f:
        sum_ += int(digit)
    return sum_


print(fac_digit_sum(100))
