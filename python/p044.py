from tqdm import tqdm


def pentagonal(n):
    # Pn = n(3n-1)/2
    return int(((n * 3 * n) - n) * 0.5)


mx = 2500
pnums = []
for i in range(1, mx + 1):
    pnums.append(pentagonal(i))

result = 0
for i, j in enumerate(tqdm(pnums)):
    for k in pnums[i:]:
        s = j + k
        d = abs(k - j)
        if s in pnums and d in pnums:
            print("\n")
            print(f"Pj: {j}")
            print(f"Pk: {k}")
            print(f"S = {j} + {k} = {s} ... OK")
            print(f"D = |{k} - {j}| = {d} ... OK")
            print("\n")
            break
    else:
        continue
    break
