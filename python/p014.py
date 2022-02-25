from tqdm import trange

starting_number = 0
longest_chain = 0

for num in trange(1, 1000000):
    n = num
    i = 1
    while n > 1:
        if n % 2 == 0:
            n = n * 0.5
        else:
            n = 3 * n + 1
        n = int(n)
        i += 1

    if i > longest_chain:
        longest_chain = i
        starting_number = num

print(
    "The number {} has a chain with a length of {}".format(
        starting_number, longest_chain
    )
)
