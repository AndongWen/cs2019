class Node(object):
	def __init__(self, elem, next_ = None, pre = None):
		self.elem = elem
		self.next_ = next_
		self.pre = pre 


class DoubleLinkList(object):
	def __init__(self):
		self.__head = None
	
	def is_empty(self):
		return self.__head == None

	def length(self):
		cur = self.__head
		if cur == None:
			return 0
		else: 
			count = 1 
			while cur.next_ != self.__head: 
				count += 1 
				cur = cur.next_ 
		return(count) 

	def travell(self):
		cur = self.__head
		if cur is None:
			return '''空链表'''
		else:
			# 此种循环一定会漏掉最后一个
			while cur.next_ != self.__head:
				print(cur.elem, end = " ")
				cur = cur.next_
		print(cur.elem, end = " ")

	def prepend(self, elem):
		node = Node(elem)
		if self.is_empty():
			self.__head = node
			node.next_ = node
			node.pre = node
		else:
			cur = self.__head
			while cur.next_ != self.__head:
				cur = cur.next_
			self.__head.pre = node 
			node.next_ = self.__head
			self.__head = node
			cur.next_ = node
			node.pre = cur

	def append(self, elem):
		cur= self.__head
		if cur == None:
			node = Node(elem)
			self.__head = node
			node.next_ = node
			node.pre = node
			return
		while cur.next_ != self.__head:
			cur = cur.next_
		node = Node(elem)
		cur.next_ = node
		node.next_ = self.__head
		node.pre = cur
		self.__head.pre = node

	def insert(self, pos, elem):
		# pos从0开始
		pre = self.__head
		count = 0
		if pos <= 0:
			self.perpend(elem)
			return
		if pos > (self.length()-1):
			self.append(elem)	
			return
		while count < pos-1:
			count += 1
			pre = pre.next_
		node = Node(elem)
		node.next_ = pre.next_
		pre.next_.pre = node
		pre.next_ = node
		node.pre = pre
		
	def remove(self, elem):
#		自己的写法 比较混乱
		cur = self.__head
		if cur is None:
			return """空"""
#		if cur.elem == elem:
#			if cur.next_ == cur:
#				self.__head =None
#				return
#			else:
#				self.__head = cur.next_
#				while cur.next_ != self.__head:
#					cur = cur.next_
#				cur.next_ = self.__head
#				return
#		while cur.elem != elem:
#			pre = cur 
#			cur = cur.next_
#			if cur == self.__head:
#				return
#		pre.next_ = cur.next_
		while cur.next_ != self.__head:
			#从头到尾遍历
			if cur.elem == elem:
				#是否为头元素
				if cur == self.__head:
					# 找尾节点
					rear = self.__head
					while rear.next_ != self.__head:
						rear = rear.next_
					self.__head = self.__head.next_
					self.__head.pre = rear
					rear.next_ = self.__head
					return
				else:
					#为中间元素
					cur.pre.next_ = cur.next_
					cur.next_.pre = cur.pre
					return
			else:	
				cur = cur.next_
		#处理最后一个元素
		if cur.elem == elem:
			#判断是否只有一个元素
			if cur == self.__head:
				self.__head = None
			else:	
				cur.pre.next_ = self.__head
				self.__head.pre = cur.pre 
			return
		else:
			return """不存在""" 

	def search(self, elem):
		cur = self.__head
		if cur is None:
			return "空列表"
		while cur.elem != elem:
			cur = cur.next_
			if cur == self.__head:
				return False
		return True
		

	
def main():
	dll = DoubleLinkList()
	print(dll.is_empty())
	dll.prepend(4)
	dll.append(7)
	dll.travell()
	dll.insert(5, 4)
	print('*******')
	dll.travell()
	print('*******')
	print(dll.search(45))
	dll.insert(2, 9)
	dll.append(1)
	dll.append(2)
	dll.append(3)
	dll.append(4)
	dll.append(5)
	dll.append(6)
	dll.travell()
	print('*******')
	dll.remove(4)
	dll.travell()

if __name__ == "__main__":
	main()
