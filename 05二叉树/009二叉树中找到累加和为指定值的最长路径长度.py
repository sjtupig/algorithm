'''
路径是指从某个节点往下，最多选择一个孩子或者不选锁形成的路径

'''
class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None 
		self.right = None 
		

def getmaxlength(root, totalsum):
	lengthMap = {}
	lengthMap.update({0:0})
	return preOrder(root, 0, totalsum, 1, lengthMap, 0)


def preOrder(root, presum, totalsum, level, lengthMap, maxLength):
	if not root:return maxLength
	cursum = presum+root.val 
	if cursum not in lengthMap:
		lengthMap[cursum] = level
	if (cursum-totalsum) in lengthMap:
		maxLength = max(maxLength, level-lengthMap[cursum-totalsum])
	maxLength = preOrder(root.left, cursum, totalsum, level+1, lengthMap, maxLength)
	maxLength = preOrder(root.right, cursum, totalsum, level+1, lengthMap, maxLength)
	if lengthMap[cursum] == level:
		lengthMap.pop(cursum)
	return maxLength

head = TreeNode(-3)
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(0)
d = TreeNode(1)
e = TreeNode(6)
f = TreeNode(-9)
g = TreeNode(2)
h = TreeNode(1)
head.left = a
head.right = f 
a.left = b 
a.right = c 
c.left = d 
c.right = e 
f.left = g 
f.right = h 
print(getmaxlength(head,6))
print(getmaxlength(head,9))