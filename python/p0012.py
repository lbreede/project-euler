def main():
	i = 1
	while True:

		triangle_num = calcTriangleNumber(i)
		factor_set = calcFactors(triangle_num)
		num_factors = len(factor_set)
		print(num_factors)
		if num_factors > 500:
			print(f"FOUND: {triangle_num} has {num_factors} factors!")
			break
		i += 1 # TOO SLOW!

def calcTriangleNumber(num):
	tri = 0
	for x in range(1, num+1):
		tri += x
	return tri

def calcFactors(num):
	fac = set()
	for x in range(1, num+1):
		if num % x == 0:
			fac.add(x)

	return fac

if __name__ == "__main__":
	main()