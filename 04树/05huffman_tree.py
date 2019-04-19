class BinTNode(object):
	'''二叉树的节点类'''
	def __init__(self, data, lchild = None, rchild = None):
		self.data = data
		self.lchild = lchild
		self.rchild = rchild		


class PrioQueueError(ValueError):
	pass


class PrioQueue(object):
	def __init__(self, a = []):
		self._elems = list(a)
		if self._elems:
			self.buildheap()

	def is_empty(self):
		return self._elems is None
	
	def num(self):
		return len(self._elems)

	def peek(self):
		if self.is_empty():
			raise PrioQueueError('in peek')
		return self._elems[0]
	
	def enqueue(self, e):	
		self._elems.append(None)
		self.select_up(e, len(self._elems)-1)

	def select_up(self, e, end):
		elems, i, j = self._elems, end, (end-1)//2
		while i > 0 and e < elems[j]:
			elems[i] = elems[j]
			i, j = j, (j-1)//2
		elems[i] = e

	def dequeue(self):
		if self.is_empty():
			raise PrioQueueError('in dequeue')
		elems = self._elems
		de_e = elems[0] # 此元素不能直接弹出
		e = elems.pop()
		if len(elems) > 0:
			self.select_down(e, 0, len(elems)) 
		return de_e
		
	def select_down(self, e, begin, end): # begin不直接写死,方便后面的buildheap调用
		elems, i, j = self._elems, begin, 2*begin+1
		while j < end:
			if j+1 < end and elems[j] > elems[j+1]:
				j += 1
			if e < elems[j]:
				break
			elems[i] = elems[j]
			i, j = j, 2*j+1
		elems[i] = e
	
	def buildheap(self):
		end = len(self._elems)
		for i in range(end//2, -1, -1):
			select_down(elems[i], i, end)


class HuffmanPrioQueue(PrioQueue):
	pass


class HTNode(BinTNode):
	def __lt__(self):
		return self.data < othernode.data


def huffmantree(weights):
	h = HuffmanPrioQueue()
	for i in weights:
		h.enqueue(HTNode(i))
	while h.num() > 1:
		t1 = h.dequeue()
		t2 = h.dequeue()
		x = t1.data + t2.data
		h.enqueue(HTNode(x, t1, t2))
	return h.dequeue()
