def qsort_rec(lst, l, r):
	'''两个指针：头指针与尾指针，小记录在左边，大记录在右边'''
	if l >= r:
		return # 递归出口
	i = l
	j = r
	k = lst[i] # 记录初始值 lst[i]为初始空位
	while i < j:
		while i < j and lst[j] >= k:
			j -= 1
		if i < j: # 小记录移动到左边
			lst[i] = lst[j] # 移动时产生不稳定
			i += 1
		while i < j and lst[i] < k:
			i +=1
		if i < j: # 大记录移动到右边
			lst[j] = lst[i]
			j -= 1
	lst[i] = k
	qsort_rec(lst, l, i-1)
	qsort_rec(lst, i+1, r)


def qsort_rec1(lst, begin, end):
	'''两个指针，列表分为三段,小记录段，大记录端，未排序端
		第一个指针指向小记录的末端，第二个指针指向第一个未排序的
		元素'''
	if begin >= end:
		return	
	k = lst[begin]
	i = begin
	for j in range(begin+1, end+1):
		if lst[j] < k: # 发现小元素后，交换小元素
			i += 1 
			lst[i], lst[j] = lst[j], lst[i]	
	lst[begin], lst[i] = lst[i], lst[begin] # 将轴元素放置好
	qsort_rec1(lst, begin, i-1)
	qsort_rec1(lst, i+1, end)
	
def quick_sort(lst):
	'''选取一个标准，把比他大的放在表的右边，比他小的放在表的左边，然后将这两部分依次划分下去，直到每个部分最多只有一个元素'''
	n = len(lst)
	qsort_rec1(lst, 0, n-1)


def main():
	a = [1,0,2,9,41,55,62,3,5,63,622,5,3,8,7,4,6,5,235,654,2232,7232,214,1,6,72,847,13,13]
	# a = [0,1,2,3,4,5,6,7,8,9,9]
	quick_sort(a)
	for i in a:
		print(i, end = ' ')
	print('')


if __name__ == "__main__":
	main()
