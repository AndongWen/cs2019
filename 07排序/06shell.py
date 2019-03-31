def shell_sort(a):
	'''基于插入排序'''
	n = len(a)
	gap = n//2
	while gap > 0:
		for i in range(gap, n):
			j = i
			k = a[i]
			while j > 0 and a[j-gap] > k:
				a[j] = a[j-gap]
				j -= gap
			a[j] = k
		gap //= 2

	
		
def main():
	a = [9,0,1,3,2,5,7,4,8,6]
	shell_sort(a)
	for i in a:
		print(i, end = " ")
	print('')


if __name__ == "__main__":
	main()
