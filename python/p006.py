def sum_of_squares(n: int) -> int:
    return sum([x * x for x in range(1, n + 1)])


def square_of_sums(n: int) -> int:
    return sum(range(1, n + 1)) ** 2


def sum_square_difference(n: int) -> int:
    return square_of_sums(n) - sum_of_squares(n)


def main() -> None:
    answer = sum_square_difference(100)
    print("Project Euler - Sum Square Difference (Problem 6)")
    print(f"Answer: {answer:,}")


if __name__ == "__main__":
    main()
