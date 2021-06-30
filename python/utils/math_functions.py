from math import sqrt

# def mrange(start, stop, step):
#     while start < stop:
#         yield start
#         start += step

def is_prime(num):
    """Checks if parsed number is a prime number.

    Args:
        num: The number to be checked. Preferably an integer.

    Returns:
        A boolean whether the parsed number is a prime (True) or not (False).
    """
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    # return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))