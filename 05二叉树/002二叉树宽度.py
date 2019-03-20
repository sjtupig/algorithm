class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None 

'''
队列实现，先进先出
'''
class Solution:
    def TreeWidth(self, pRoot):
        # write code here

        if not pRoot:return 0 
        stack = []
        width = 1
        if pRoot.left:stack.append(pRoot.left)
        if pRoot.right:stack.append(pRoot.right)
        while stack:
        	width = max(width,len(stack))
        	for i in range(len(stack)):
        		t = stack.pop(0)
        		if t.left:stack.append(t.left)
        		if t.right:stack.append(t.right)

        return width
phead = TreeNode(1)
phead.left = TreeNode(2)
phead.right = TreeNode(3)
phead.left.left = TreeNode(4)
phead.left.right = TreeNode(5)
phead.right.left = TreeNode(6)
phead.right.right = TreeNode(7)
sol = Solution()
print(sol.TreeWidth(phead))	