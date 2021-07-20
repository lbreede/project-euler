with open("p0013_input.txt", "r") as f:
	numbers = [int(x) for x in f.read().split("\n")]
	
result = str(sum(numbers))[:10]
print(result)