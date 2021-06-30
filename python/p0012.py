def main():
	num = 1
	while True:
		tri = calc_triange(num)
		fac = count_factors(tri)
		print(fac)
		if fac > 500:
			print(tri)
			break
		num += 1 #????

def calc_triange(num):
	tri = 0
	for x in range(1, num+1):
		tri += x
	return tri

def count_factors(num):
	count = 0
	for x in range(1, num+1):
		if num % x == 0:
			count += 1
	return count

if __name__ == "__main__":
	main()