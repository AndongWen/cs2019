def heap_sort(elems):
	def select_down(elems, e, begin, end):
		i, j = begin, 2*begin+1
		while j < end:
			if j+1 < end and elem[j] > elem[j+1]:
				j += 1
			if e < elem[j]:
				break
			elem[i] = elem[j]
			i, j = j, 2*j+1
		elem[i] = e

	end = len(elems)
	for i in range(end//2, -1, -1): # 对原来的列表进行建堆
		select_down(elems, elem[i], i, end)
	for i in range((end-1), 0, -1): # 每次取出一个元素并将新元素放入进行排序 O(nlogn)
		e = elems[i]
		elems[i] = elems[0]
		select_down(elems, e, 0, i)
