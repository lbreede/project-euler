from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

def main():
    sum_ = 0
    for x in range(2000000):
        if is_prime(x):
            sum_ += x

    print(sum_)

if __name__ == "__main__":
    main()