from math import sqrt


def is_prime(num):
    """Checks if parsed number is a prime number.

    Args:
        num: The number to be checked. Preferably an integer.

    Returns:
        Boolean whether the parsed number is a prime number (True) or not
            (False).
    """
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    # return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))


def triangle(n):
    """Returns the triangle number of n using tn = ½n(n+1)

    Args:
        n: The number

    Returns:
        The triangle number of n

    """
    return int(0.5 * n * n + 0.5 * n)
