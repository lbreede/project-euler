def smallest_multiple(start: int, stop: int) -> int:
    smallest_evenly_divisible = stop

    while True:
        success = 0
        for x in range(start, stop + 1):
            if smallest_evenly_divisible / x % 1 == 0:
                success += 1

        if success == stop:
            break
        else:
            smallest_evenly_divisible += stop

    return smallest_evenly_divisible


x = smallest_multiple(1, 20)
print(x)
