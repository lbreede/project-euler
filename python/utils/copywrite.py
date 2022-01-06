import os

COPYWRITE = "#\n\
# Solution to Project Euler Problem {}\n\
# Copyright (c) Lennart Breede. All rights reserved.\n\
# https://github.com/lbreede/project-euler\n\
#\n\n"

for i in range(2, 100):

	file = f"../p{str(i).zfill(3)}.py"

	if os.path.isfile(file):
		with open(file) as f:
			temp = f.read()
		
		firsts = set()
		for line in temp.split("\n")[:5]:
			if len(line) != 0:
				firsts.add(line[0])
			else:
				firsts.add("")

		if len(firsts) == 1 and list(firsts)[0] == "#":
			print("don't do anything")
		else:
			with open(file, "w") as f:
				f.write(COPYWRITE.format(i) + temp)

	# else:
	# 	print("File does not exist!")

print()