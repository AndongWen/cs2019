# python 中列表使用的是分离体结构，元素外置，自带自动增长
class SStack(object):
	def __init__(self):
		self.__elems = []
	# 如何创建一个规定长度的列表？？？

	def is_empty(self):
		return self.__elems == []

	def push(self, elem):
		self.__elems.append(elem)
	
	def pop(self):
		if self.is_empty():
			return "error"
		else:
			return self.__elems.pop()
		
	def top(self):
		if self.is_empty():
			return "error"
		else:
			return self.__elems[-1]
		


def main():
	stack = SStack()
	print(stack.is_empty())
	stack.push(4)
	print(stack.is_empty())
	stack.pop()
	print(stack.is_empty())
	stack.push(4)
	stack.push(5)
	stack.push(7)
	stack.push(9)
	stack.push(0)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	

if __name__ == "__main__":
	main()
