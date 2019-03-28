def Josephus(n, k ,m):
	people = list(range(1,n+1))

	# num为列表的长度， i为下标
	num, i = n, k-1
	for num in range(n, 0 ,-1):
		# 每次删除一个元素，其后的所有元素的下标会前移,即从下标为第i-1后的元素计数
		i = (i+m-1)%num
		print(people.pop(i), end = (', ' if num > 1 else '\n'))
	return



def main():
	Josephus(10, 2, 7)


if __name__ == "__main__":
	main()
