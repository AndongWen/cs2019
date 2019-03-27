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
		cur_node = self._head
		if cur_node == None:
			return 0
		else: 
			count = 1 
			while cur_node.next_ != self._head: 
				count += 1 
				cur_node = cur_node.next_ 
		return(count) 

	def travell(self):
		cur_node = self._head
		if cur_node is None:
			return
		else:
			while cur_node.next_ != self._head:
				print(cur_node.elem, end = " ")
				cur_node = cur_node.next_
		print(cur_node.elem, end = " ")

	def prepend(self, elem):
		node = Node(elem)
		if self.is_empty():
			self._head = node
			node.next_ = node
		else:
			cur_node = self._head
			while cur_node.next_ != self._head:
				cur_node = cur_node.next_
			node.next_ = self._head
			self._head = node
			cur_node.next_ = node

	def append(self, elem):
		cur_node= self._head
		if cur_node == None:
			node = Node(elem)
			self._head = node
			node.next_ = node
			return
		while cur_node.next_ != self._head:
			cur_node = cur_node.next_
		node = Node(elem)
		cur_node.next_ = node
		node.next_ = self._head

	def insert(self, pos, elem):
		# pos从0开始
		pre_node = self._head
		count = 0
		if pos <= 0:
			self.perpend(elem)
			return
		if pos > (self.length()-1):
			self.append(elem)	
		while count < pos-1:
			count += 1
			pre_node = pre_node.next_
		node = Node(elem)
		node.next_ = pre_node.next_
		pre_node.next_ = node

	def remove(self, elem):
#		自己的写法 比较混乱
		cur_node = self._head
		pre_node = None
		if cur_node is None:
			return """空"""
#		if cur_node.elem == elem:
#			if cur_node.next_ == cur_node:
#				self._head =None
#				return
#			else:
#				self._head = cur_node.next_
#				while cur_node.next_ != self._head:
#					cur_node = cur_node.next_
#				cur_node.next_ = self._head
#				return
#		while cur_node.elem != elem:
#			pre_node = cur_node 
#			cur_node = cur_node.next_
#			if cur_node == self._head:
#				return
#		pre_node.next_ = cur_node.next_
		while cur_node.next_ != self._head:
			#从头到尾遍历
			if cur_node.elem == elem:
				#是否为头元素
				if cur_node == self._head:
					# 找尾节点
					rear = self._head
					while rear.next_ != self._head:
						rear = rear.next_
					self._head = self._head.next_
					rear.next_ = self._head
					return
				else:
					#为中间元素
					pre_node.next_ = cur_node.next_
					return
			else:	
				pre_node = cur_node
				cur_node = cur_node.next_
		#处理最后一个元素
		if cur_node.elem == elem:
			#判断是否只有一个元素
			if cur_node == self._head:
				self._head = None
			else:	
				pre_node.next_ = self._head
			return
		else:
			return """不存在""" 

	def search(self, elem):
		cur_node = self._head
		pre_node = None
		if cur_node is None:
			return "空列表"
		while cur_node.elem != elem:
			per_node = cur_node 
			cur_node = cur_node.next_
			if cur_node == self._head:
				return False
		return True
		

	
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

if __name__ == "__main__":
	main()
