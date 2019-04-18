class StackUnderFlow(ValueError):
	pass


class SStack(object): # 用于辅助树的非递归遍历
	'''顺序表实现的栈'''
	def __init__(self):
		self._elems = []
	
	def is_empty(self):
		return self._elems == []
	
	def top(self):
		if self.is_empty():
			raise StackUnderFlow('in top')
		return self._elems[-1]

	def push(self, data):
		self._elems.append(data)

	def pop(self):
		if self.is_empty():
			raise StackUnderFlow('in pop')
		return self._elems.pop()


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

	def pre_order(self):
		'''
			先序遍历(非递归)
			栈用于保存尚未遍历的右子树
			外循环的条件:当前的树非空或栈非空
			内循环:当前树不为空，他需要一直下行找到最下最左的节点，
					并一路将右子树压栈,为空时，回溯
		'''
		s = SStack()
		t = self.root
		while t is not None or not s.is_empty():
			while t is not None:
				print(t.data, end =' ')
				s.push(t.rchild) # 将右子树压栈，其可能为空
				t = t.lchild # 继续下行
			t = s.pop() # 处理右子树
							
	def mid_order(self):
		'''
			中序遍历(非递归)
			第一个访问的节点即是整颗树中最左边的节点
			外循环的条件:当前的树非空或栈非空
			内循环:当前树不为空，他需要一直下行找到最下最左的节点，
					并一路途径的节点压栈
			'''
		s = SStack()
		t = self.root
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t)
				t = t.lchild
			t = s.pop() # 从某种程度上说左节点就是父节点
			print(t.data, end = ' ')
			t = t.rchild

	def post_order(self):
		'''
			后序遍历(非递归)
			第一个访问的节点即是整颗树中最下面的最左边的节点
			外循环的条件:当前的树非空或栈非空
			内循环:当前树不为空，他需要一直下行找到最下最左的节点，
					并一路将途径的节点压栈	
			特点：若正在处理的节点不为空，则栈顶节点即为父节点
									为空，栈顶节点就是要访问的节点
			'''
		s = SStack()
		t = self.root
		while t is not None or not s.is_empty():
			while t is not None:
				s.push(t)
				# 能左就左下，否则右下
				t = t.lchild if t.lchild is not None else t.rchild	
			t = s.pop()
			print(t.data, end = ' ')
			if not s.is_empty() and t == s.top().lchild: # 两者顺序不可颠倒
				t = s.top().rchild # 转到右子树
			else:
				t = None # 实质为无右子树，或右子树遍历完毕转向栈顶元素，即其父节点


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
	t.pre_order()
	print('*****')
	t.mid_order()
	print('*****')
	t.post_order()
	print('*****')


if __name__ == "__main__":
	main()
