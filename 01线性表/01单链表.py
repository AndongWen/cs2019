class Node(object):
	def __init__(self, elem, next_ = None):
		self.elem = elem
		self.next_ = next_


class SingLinkList(object):
	def __init__(self):
		self._head = None
	
	def is_empty(self):
		return self._head == None

	def length(self):
		count = 0
		cur_node = self._head
		while cur_node != None:
			count += 1
			cur_node = cur_node.next_
		return(count)

	def travell(self):
		cur_node = self._head
		while cur_node != None:
			print(cur_node.elem, end = " ")
			cur_node = cur_node.next_

	def prepend(self, elem):
		node = Node(elem)
		node.next_ = self._head
		self._head = node
		# 另一种写法
		# self._head = Node(elem,self._head)
		

	def append(self, elem):
		cur_node= self._head
		if cur_node == None:
			self.prepend(elem)
			return
		while cur_node.next_ != None:
			cur_node = cur_node.next_
		node = Node(elem)
		cur_node.next_ = node

	def insert(self, pos, elem):
		pre_node = self._head
		count = 0
		if pos <= 0:
			self.perpend(elem)
			return
		if pos >= self.length():
			self.append(elem)	
		while count < pos-1:
			count += 1
			pre_node = pre_node.next_
		node = Node(elem)
		node.next_ = pre_node.next_
		pre_node.next_ = node

	def remove(self, elem):
		cur_node = self._head
		pre_node = None
		if cur_node is None:
			return
		if cur_node.elem == elem:
			self._head = cur_node.next_
			return
		while cur_node.elem != elem:
			pre_node = cur_node 
			cur_node = cur_node.next_
			if cur_node == None:
				return
		pre_node.next_ = cur_node.next_

	def search(self, elem):
		cur_node = self._head
		if cur_node is None:
			return """空"""
		while cur_node.elem != elem:
			cur_node = cur_node.next_
			if cur_node == None:
				return False
		return True
		
	def rev(self):
		'''链表反转'''
		'''将一个链表的首节点不断取下，将其插入到另一个链表'''
		p = None
		if self._head is None:
			return '''列表weikong'''
		while self._head is not None:
			q = self._head
			self._head = q.next_
			q.next_ = p
			p = q
		self._head = p

	def sort(self):
		'''插入排序(移动元素)'''
		if self._head is None:
			return '''链表为空，无法排序'''
		# 用于标记正在排序的节点,从第二个开始
		p = self._head.next_
		while p is not None:
			# 用于对前面有序段。寻找一个正确的位置
			q = self._head
			x = p.elem
			while q != p and q.elem <= x:
				q = q.next_
			while q != p:
				y = q.elem
				q.elem = x
				x = y
				q = q.next_
			p.elem = x	
			p = p.next_
			 
	def sort2(self):
		'''插入排序(更改链接)'''
		'''实际处理为一个个取下链表节点，将其插入到一段元素递增的节点链中正确的位置中'''
		p = self._head
		# 只有一个元素或为空，无需排序
		if p is None and p.next_ is None:
			return 
		
		rem = p.next_ # 排序从第二开始
		p.next_ = None # 将有序部分的末尾设置
		while rem is not None:
			i = self._head
			j = None
			# 有序部分的遍历
			while i != None and i.elem <= rem.elem:
				j = i
				i = i.next_
			# 是否在表头插入
			if j is None:
				self._head = rem
			else:
				j.next_ = rem
			j = rem
			rem = rem.next_
			j.next_ = i
	
def main():
	sll = SingLinkList()
	print(sll.is_empty())
	sll.append(1)
	print(sll.is_empty())
	sll.prepend(2)
	sll.travell()
	sll.append(3)
	sll.append(4)
	sll.append(5)
	sll.append(6)
	sll.append(7)
	print("**********")
	print(sll.length())
	sll.travell()
	sll.insert(4,4)
	print("**********")
	sll.travell()
	print(sll.search(98))
	print(sll.search(4))
	sll.remove(4)
	print("**********")
	sll.travell()
	print("**********")
	print(sll.length())
	sll.rev()
	sll.travell()
	print("**********")
	#sll.sort()
	sll.sort2()
	sll.travell()

if __name__ == "__main__":
	main()
