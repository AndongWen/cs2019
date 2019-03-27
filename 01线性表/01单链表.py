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
