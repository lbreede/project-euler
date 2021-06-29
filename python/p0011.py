with open("p0011_input.txt", "r") as f:
	line_list = f.read().split("\n")

grid_list = []
for line in line_list:
	grid_list.append(line.split())

print(grid_list)