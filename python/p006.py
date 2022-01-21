def main():
    max_ = 100

    return squareOfSum(max_) - sumOfSquares(max_)


def sumOfSquares(max_):
    result = 0
    for x in range(1, max_ + 1):
        result += x * x

    return result


def squareOfSum(max_):
    result = 0
    for x in range(1, max_ + 1):
        result += x

    return result * result


if __name__ == "__main__":
    print(main())
