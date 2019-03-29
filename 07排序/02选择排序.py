def select_sort(a):
	''' 将列表分成两个部分，从无序部分中找到最小的元素，将其放到前面，自然成为有序部分'''
	n = len(a)
	for j in range(n-1):
		min = j
		for i in range(j, n-1):
			if a[min] > a[i+1]:
				min = i+1
		a[j], a[min] = a[min], a[j]


def main():
	a = [1,0,2,9,3,8,7,4,6,5]
	select_sort(a)
	for i in a:
		print(i, end = ' ')
	print('')


if __name__ == "__main__":
	main()
