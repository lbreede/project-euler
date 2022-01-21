# Sub-string divisibility

from itertools import permutations


def sub_string(num, start, rng):
    start -= 1
    end = start + rng
    # strnum = str(num)
    return int(num[start:end])


def check_properties(num):
    p1 = sub_string(num, 2, 3) % 2 == 0
    p2 = sub_string(num, 3, 3) % 3 == 0
    p3 = sub_string(num, 4, 3) % 5 == 0
    p4 = sub_string(num, 5, 3) % 7 == 0
    p5 = sub_string(num, 6, 3) % 11 == 0
    p6 = sub_string(num, 7, 3) % 13 == 0
    p7 = sub_string(num, 8, 3) % 17 == 0

    return [p1, p2, p3, p4, p5, p6, p7]


nums = "1234567890"
permutations = list(permutations(nums))
permutations = [''.join(permutation) for permutation in permutations]

result = 0

for p in permutations:
    if all(check_properties(p)):
        result += int(p)

print(result)
