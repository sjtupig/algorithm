class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None 
'''
思想和求最大路径和一样，该节点要么是最大距离的跟，要是是最大距离的经过的
另外可以参考https://www.cnblogs.com/miloyip/archive/2010/02/25/1673114.html

'''
class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		self.maxlength = 0


	def p(self, root):
		if not root:return -1 #这里必须是-1，叶子节点计算其长度时应该是0，max(left, right)+1时-1和+1刚好为0
		left = self.p(root.left)
		right = self.p(root.right)
		self.maxlength = max(self.maxlength, left+right+2)
		return max(left, right)+1

	def getmaxlengh(self, root):
		self.p(root)
		return self.maxlength

phead = TreeNode(1)
phead.left = TreeNode(2)
phead.right = TreeNode(3)
phead.left.left = TreeNode(4)
phead.left.right = TreeNode(5)
phead.right.left = TreeNode(6)
phead.right.right = TreeNode(7)
phead.right.left.left = TreeNode(10)
sol = Solution()
print(sol.getmaxlengh(phead))	