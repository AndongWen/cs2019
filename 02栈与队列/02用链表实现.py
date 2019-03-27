class Node(object):
	def __init__(self, elem, next = None):
		self.elem = elem
		self.next_ = next

class LStack(object):
	def __init__(self):
		self.__top = None

	def is_empty(self):
		return self.__top == None
	
	def push(self, elem):
		node = Node(elem, self.__top)	
		self.__top = node
	
	def pop(self):
		if self.is_empty():
			return '出错，栈为空'
		else:
			pop_elem = self.__top.elem
			self.__top = self.__top.next_
			return pop_elem
	
	def top(self):
		if self.is_empty():
			return '栈为空'
		else:
			return self.__top.elem


def main():
	lstack = LStack()
	print(lstack.is_empty())
	lstack.push(4)
	print(lstack.is_empty())
	lstack.push(9)
	print(lstack.pop())
	print(lstack.top())
	
	lstack.push(1)
	lstack.push(2)
	lstack.push(3)
	lstack.push(4)
	lstack.push(5)
	lstack.push(6)
	print(lstack.pop())
	print(lstack.pop())
	print(lstack.pop())
	print(lstack.pop())
	print(lstack.pop())
	print(lstack.pop())
	print(lstack.pop())
	print(lstack.pop())


if __name__ == "__main__":
	main()
