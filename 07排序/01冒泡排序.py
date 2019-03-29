def bubble_sort(a):
	for j in range(len(a), 0, -1):
		for i in range(0, j-1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
		

def main():
	a = [9,0,1,3,2,5,7,4,8,6]
	bubble_sort(a)
	for i in a:
		print(i, end = " ")
	print('')


if __name__ == "__main__":
	main()
