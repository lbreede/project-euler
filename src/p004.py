from tqdm import trange


def split_even_string(string: str) -> tuple[str, str]:
    length = len(string)
    front = string[: length // 2]
    back = string[length // 2 :]
    return front, back


def mirror_and_compare(front: str, back: str) -> bool:
    if int(front) == int(back[::-1]):
        return True
    return False


def main() -> None:
    start = 1000
    largest_palindrome = 0

    for x in trange(1, start):
        for y in range(1, start):
            a = start - x
            b = start - y

            c = a * b

            if len(str(c)) % 2 != 0:
                continue

            front, back = split_even_string(str(c))
            if not mirror_and_compare(front, back):
                continue

            if c > largest_palindrome:
                largest_palindrome = c

    print(largest_palindrome)


if __name__ == "__main__":
    main()
