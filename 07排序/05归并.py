def merge(old, new, low, mid, high):
	'''用于相邻的两个子序列的归并'''
	''' old:原来的列表
		new:用来转移用的新列表
		low, mid, high:两个子序列的下标，采用左开右闭'''
	i, j, k = low, mid, low
	while i < mid and j < high:
		if old[i] <= old[j]:
			new[k] = old[i]
			i += 1
		else:
			new[k] = old[j]
			j += 1
		k += 1
	# 上述循环结束时，两个子序列必有一个其中的元素没有全部转移完，此时只要
	# 将剩余部分复制过去即可
	while i < mid:
		new[k] = old[i]
		i += 1
		k += 1
	while j < high:
		new[k] = old[j]
		j += 1
		k += 1
	

def merge_pass(old, new, slen, flen):
	'''用于对原列表的遍历，依次对相邻的子序列做归并，考虑不规则的情况'''
	''' old:原来的列表
		new:用来转移用的新列表
		slen:子序列的长度
		flen:原序列的长度'''
	i = 0 # 用于标记未归并的第一个元素
	while i + slen*2 < flen:
		merge(old, new, i, i+slen, i+slen*2)
		i += slen*2
	# 处理不规则的情况
	if i + slen < flen:	# 仍然有两个子序列，只是第二个子序列长度不到slen
		merge(old, new, i, i+slen, flen)
	else: # 只有一个子序列
		for j in range(i, flen):
			new[j] = old[j]
	

def merge_sort(a):
	''' 将一个序列看成n个有序的子序列组成，然后让相邻的两个子序列依次归并
		子序列长度翻倍，原序列中子序列的数目减半，直到子序列的数目为1，
		归并才结束'''
	flen = len(a)
	slen = 1
	b = [None] * flen # 构造一个新的与原来序列等长的序列	
	while slen < flen:
		merge_pass(a, b, slen, flen)
		slen *= 2
		merge_pass(b, a, slen, flen) # 调换两个表的角色 同时如果在上一次遍历过程中，序列已经达到有序，此次遍历就是将结果存回原位
		slen *= 2
	

def merge_sort1(list):
	'''第二种版本'''
	n = len(list)
	if n <= 1:
		return
	mid = n//2
	left_li = merge_sort1(list[:mid])
	right_li = merge_sort1(list[mid:])
	left_p = right_p = 0
	result = []
	while left_p < len(left_li) and right_p < len(right_li):
		if left_li[left_p] <= right_li[right_p]:
			result.append(left_li[left_p])
			left_p += 1
		else:
			result.append(right_li[right_p])
			right_p += 1
	result += left_li[left_p:]
	result += right_li[right_p:]
	return result
			
def main():
	a = [1,0,2,9,3,8,7,4,6,5]
	merge_sort(a)
	# merge_sort(a)
	for i in a:
		print(i, end = ' ')
	print('')


if __name__ == "__main__":
	main()
