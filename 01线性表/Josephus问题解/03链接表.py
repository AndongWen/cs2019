class SLNode(object):
	def __init__(self, elem, next_ = None):
		self.elem = elem
		self.next_ = next_


class SCLink(object):
	'''单向循环链表-表对象的数据域只指向链表的尾部，可以做到对
	表头和表尾的操作时间复杂度都为O（1）'''
	def __init__(self):
		self._rear = None

	def is_empty(self):
		return self._rear is None
	
	def length(self):
		count = 0
		if self.is_empty():
			return count
		else:
			p = self._rear.next_
			while p.next_ != self._rear:
				count += 1
				p = p.next_
			count += 1
			return count

	def prepend(self, elem):
		p = SLNode(elem)
		if self._rear is None:
			self._rear = p
			p.next_ = p
			return
		else:
			p.next_ = self._rear.next_
			self._rear.next_ = p
			return

	def pop_first(self):
		if self._rear is None:
			return '''弹出首元素：列表为空'''
		elif self._rear != self._rear.next_:
			e = self._rear.next_.elem
			self._rear.next_ = self._rear.next_.next_
			return e
		else:
			'''表中只有一个元素'''
			e = self._rear.elem
			self._rear = None
			return e

	def append(self, elem):
		p = SLNode(elem)
		if self._rear is None:
			self._rear = p
			p.next_ = p
			return
		else:
			p.next_ = self._rear.next_
			self._rear.next_ = p
			self._rear = p
			return
		
	def pop(self):
		if self._rear is None:
			return '''弹出末尾元素：列表为kong'''
		elif self._rear.next_ == self._rear:
			e = self._rear.elem
			self._rear = None
			return e
		# 需要找到self._rear前面一个元素
		else:
			e = self._rear.elem
			p = self._rear.next_
			while p.next_ != self._rear:
				p = p.next_
			p.next_ = self._rear.next_
			self._rear = p
			return e
 
	def insert(self, elem, pos):
		'''pos从0开始，类似索引'''
		if pos <= 0:
			return self.prepend(elem)
		elif pos >= self.length() -1:
			return self.append(elem)
		else:
			p = self._rear.next_
			q = None
			n = SLNode(elem)
			count = 0
			while count != pos:
				count += 1
				q = p
				p = p.next_
			q.next_ = n
			n.next_ = p	

	def search(self, elem):
		p = self._rear.next_
		if p is None:	
			return '''搜索时：列表为空'''
		count = 0
		while p.elem != elem:
			p = p.next_
			count += 1
			if p == self._rear:
				return -1
		return count	
			
	def remove(self, elem):
		'''删除第一个'''
		p = self._rear.next_
		q = None
		count = 0
		if p is None:	
			return -2
		while p.elem != elem:
			count += 1
			q = p
			p = p.next_
			if p == self._rear:
				return -1
		if p.next_ == p:
			self._rear = None
			return count
		else:
			q.next_ = p.next_
			return count
		
	def travell(self):	
		if self._rear is None:
			return '''遍历时，列表为空'''
		p = self._rear.next_
		while p != self._rear:
			print(p.elem, end=' ')
			p = p.next_
		print(p.elem)


class Josephus(SCLink):
	def turn(self, m):
		'''通过尾节点来定位'''
		for i in range( m):
			# 尾指针转动m次
			self._rear = self._rear.next_

	def __init__(self, n, k, m):
		SCLink.__init__(self)
		for i in range(n):
			# 实现链表的创建
			self.append(i+1)	
		self.turn(k-1)	
		while not self.is_empty():
			# 从开始位置数m-1个位置，第m个位置的节点被剔除，即头结点删除
			self.turn(m-1)
			print(self.pop_first(), end = ('\n' if self.is_empty() else ', '))
		
		
def main():
	j = Josephus(10, 2, 7)

if __name__ == "__main__":
	main()
