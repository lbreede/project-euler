def sum_of_mults(vals: tuple, max_: int) -> int:
    sum_ = 0
    for x in range(1, max_):
        for y in vals:
            if x % y == 0:
                sum_ += x
                break
    return sum_


print(sum_of_mults((3, 5), 1000))
