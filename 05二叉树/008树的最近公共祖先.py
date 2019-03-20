'''
后序遍历来判断，
当需要多次查询时，可以建一张保留各节点父节点的哈希表，然后查询A和B的最近公共祖先时，先把A的所有祖先都取出来，
然后依次看B的祖先是否在其中，第一个在其中的就是公共祖先
'''
class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def lowestAncestor(root, node1, node2):
	if not root or root == node1 or root == node2:
		return root 
	left = lowestAncestor(root.left, node1, node2)
	right = lowestAncestor(root.right, node1, node2)
	if left and right:
		return root 
	return left if left else right 

head = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)
c = TreeNode(11)
head.left = a;head.right = b; a.right = c;c.left = d; c.right = e; b.left = f; b.right = g; f.right = h; h.left = i; h.right = j
print(lowestAncestor(head,c, h)==head)
print(lowestAncestor(head,i, j)==h)