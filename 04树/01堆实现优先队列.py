class PrioQueueError(ValueError):
	pass


class PrioQueue(object):
	'''
		using heaps
		由于向上筛选需要保持其他路径保持有序-->表末尾添加
		实质为堆的性质
	'''
	def __init__(self, a = []):
		self._elems = list(a) # 做一个表的拷贝为了排除数据共享,允许任何可迭代作为参数
		if self._elems: #若列表非空，直接转变为堆
			self.buildheap()

	def is_empty(self):
		return self._elems is None

	def peek(self):
		if self.is_empty():
			raise PrioQueueError('in peek')
		return self._elems[0]

	def enqueue(self, e):
		'''入队:先在队列末尾加入None元素，避免后面交换的开销'''
		self._elems.append(None)
		self.select_up(e, len(self._elems)-1)

	def select_up(self, e, last):
		'''向上筛选，找到e的合适位置'''
		elem, i, j = self._elems, last, (last-1)//2
		while i > 0 and e < elem[j]:
			elem[i] = elem[j]
			i, j = j, (j-1)//2
		elem[i] = e

	def dequeue(self):
		if self.is_empty():
			raise PrioQueueError('in dequeue')
		elems = self._elems
		de_e = elems[0]
		e = elems.pop()
		if len(elems) > 0:
			self.select_down(e, 0, len(elems))
		return de_e

	def select_down(self, e, begin, end):
		elems, i, j = self._elems, begin, begin*2+1
		while j < end:
			if j+1 < end and elem[j] > elem[j+1]: # 判断是否有右孩子，且右孩子更小
				j += 1
			if e < elem[j]:
				break
			elem[i] = elem[j]
			i, j = j, 2*j+1
		elem[i] = e

	def buildheap(self):
		end = len(self._elems)
		for i in range(end//2, -1, -1):
			self.select_down(self._elems[i], i, end)
