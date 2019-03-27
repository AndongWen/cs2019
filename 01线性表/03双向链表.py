class Node(object):
	def __init__(self, elem, next_ = None, pre = None):
		self.elem = elem
		self.next_ = next_
		self.pre = pre


class DoubleLinkList(object):
	def __init__(self):
		self._head = None
	
	def is_empty(self):
		return self._head == None

	def length(self):
		count = 0
		cur = self._head
		while cur != None:
			count += 1
			cur = cur.next_
		return count

	def travell(self):
		cur = self._head
		while cur != None:
			print(cur.elem, end = " ")
			cur = cur.next_
		print("遍历结束")

	def prepend(self, elem):
		node = Node(elem)
		node.next_ = self._head
		self._head = node
		if node.next_ != None:
			node.next_.pre = node
		# 另一种写法
		# self._head = Node(elem,self._head)
		

	def append(self, elem):
		cur= self._head
		if cur is None:
			self.prepend(elem)
			return
		while cur.next_ != None:
			cur = cur.next_
		node = Node(elem)
		cur.next_ = node
		node.pre = cur

	def insert(self, pos, elem):
		# pos从0开始
		pre = self._head
		count = 0
		if pos <= 0:
			self.perpend(elem)
			return
		if pos >= self.length():
			self.append(elem)	
		while count < pos-1:
			count += 1
			pre = pre.next_
		node = Node(elem)
		node.next_ = pre.next_
		pre.next_.pre = node
		pre.next_ = node
		node.pre = pre

	def remove(self, elem):
#		cur = self._head
#		if cur is None:
#			return """空列表"""
#		if cur.elem == elem:
#			self._head = cur.next_
#			return
#		while cur.elem != elem:
#			pre = cur 
#			cur = cur.next_
#			if cur == None:
#				return
#		pre.next_ = cur.next_
		cur = self._head
		if cur is None:
			return """空"""
		while cur.next_ is not None:
			if cur.elem == elem:
				if cur == self._head:
					self._head = cur.next_
					cur.next_.pre = None
					return
				else:
					cur.pre.next_ = cur.next_
					cur.next_.pre = cur.pre
					return
			else:
				cur = cur.next_
		if cur.elem == elem:
			if cur == self._head:
				self._head = None
			else:
				cur.pre.next_ = None
			return
		else:
			return """找不到"""

	def search(self, elem):
		cur = self._head
		if self.is_empty():
			return """空"""
		while cur.elem != elem:
			cur = cur.next_
			if cur == None:
				return False
		return True
		

	
def main():
	sll = DoubleLinkList()
	print(sll.is_empty())
	print(sll.search(0))
	sll.append(4)
	sll.prepend(9)
	sll.travell()
	sll.prepend(3)
	sll.prepend(2)
	sll.prepend(1)
	sll.append(7)
	sll.append(8)
	sll.travell()
	sll.remove(1)
	sll.travell()
	print(sll.search(5))
	print(sll.search(9))

if __name__ == "__main__":
	main()
