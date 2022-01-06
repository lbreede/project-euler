ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("p022_names.txt") as f:
	names = f.read().split(",")

names = [x.replace("\"", "") for x in names]
names.sort()

total = 0
for i, name in enumerate(names):
	score = 0
	for letter in name:
		score += ALPHABET.index(letter) + 1
	total += (i + 1) * score

print(total)




