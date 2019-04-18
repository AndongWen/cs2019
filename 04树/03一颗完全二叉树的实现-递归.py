class BinTNode(object):
	'''二叉树的节点类'''
	def __init__(self, data, lchild = None, rchild = None):
		self.data = data
		self.lchild = lchild
		self.rchild = rchild


class Tree(object):
	'''完全二叉树的类'''
	def __init__(self):
		self.root = None

	def add(self, data):
		'''按照完全二叉树的形式依次添加节点'''
		node = BinTNode(data)
		if self.root is None:
			self.root = node
			return
		queue = [self.root]
		while queue:
			cur = queue.pop(0)
			if cur.lchild is None:
				cur.lchild = node
				return
			else:
				queue.append(cur.lchild)
			if cur.rchild is None:
				cur.rchild = node
				return
			else:
				queue.append(cur.rchild)
	
	def level_order(self):
		'''广度遍历'''
		if self.root is None:
			return '''树为空'''
		queue = [self.root] # 辅助列表，同上面添加元素作用一致
		while queue:
			cur = queue.pop(0)
			print(cur.data, end = ' ')
			if cur.lchild:
				queue.append(cur.lchild)
			if cur.rchild:
				queue.append(cur.rchild)

	def pre_order(self, node):
		'''先序遍历(递归)'''
		if node is None:
			return
		print(node.data, end = ' ')
		self.pre_order(node.lchild)
		self.pre_order(node.rchild)

	def mid_order(self, node):
		'''中序遍历(递归)'''
		if node is None:
			return
		self.mid_order(node.lchild)
		print(node.data, end = ' ')
		self.mid_order(node.rchild)

	def post_order(self, node):
		'''后序遍历(递归)'''
		if node is None:
			return
		self.post_order(node.lchild)
		self.post_order(node.rchild)
		print(node.data, end = ' ')


def main():
	t = Tree()
	t.add(0)
	t.add(1)
	t.add(2)
	t.add(3)
	t.add(4)
	t.add(5)
	t.add(6)
	t.add(7)
	t.add(8)
	t.add(9)
	t.level_order()	
	t.pre_order(t.root)
	print('*****')
	t.mid_order(t.root)
	print('*****')
	t.post_order(t.root)
	print('*****')


if __name__ == "__main__":
	main()
