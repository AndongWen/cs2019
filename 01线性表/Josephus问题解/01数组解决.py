def Josephus(n, k ,m):
	people = list(range(1, n+1))
	
	# i为下标
	i = k - 1
	for num in range(n):
		count = 0
		while count < m:
			if people[i] > 0:
				count += 1
			if count == m:
				print(people[i], end = '')
				people[i] = 0
			i = (i+1)%n
		if num < n-1:
			print(', ', end = '')
		else:
			print('')	


def main():
	Josephus(10, 2, 7)


if __name__ == "__main__":
	main()
