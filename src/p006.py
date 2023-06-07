def sum_of_squares(n: int) -> int:
    """Returns the sum of the squares of the first n natural numbers.

    Args:
        n (int): The number of natural numbers to sum.

    Returns:
        int: The sum of the squares of the first n natural numbers.

    """
    return sum([x * x for x in range(1, n + 1)])


def square_of_sums(n: int) -> int:
    """Returns the square of the sum of the first n natural numbers.

    Args:
        n (int): The number of natural numbers to sum.

    Returns:
        int: The square of the sum of the first n natural numbers.

    """
    return sum(range(1, n + 1)) ** 2


def sum_square_difference(n: int) -> int:
    """Returns the difference between the square of the sum and the sum of the squares
    of the first n natural numbers.

    Args:
        n (int): The number of natural numbers to sum.

    Returns:
           int: The difference between the square of the sum and the sum of the squares
            of the first n natural numbers."""
    return square_of_sums(n) - sum_of_squares(n)


def main() -> None:
    answer = sum_square_difference(100)
    print("Project Euler - Sum Square Difference (Problem 6)")
    print(f"Answer: {answer:,}")


if __name__ == "__main__":
    main()
