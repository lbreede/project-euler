def sum_of_mults(vals: tuple[int, ...], max_: int) -> int:
    """Returns the sum of all multiples of the given values up to the given max.

    Args:
        vals (tuple[int, ...]): The values to find multiples of.
        max_ (int): The maximum value to find multiples up to.

    Returns:
        int: The sum of all multiples of the given values up to the given max.

    """
    sum_ = 0
    for x in range(1, max_):
        for y in vals:
            if x % y == 0:
                sum_ += x
                break
    return sum_


print(sum_of_mults((3, 5), 1000))
