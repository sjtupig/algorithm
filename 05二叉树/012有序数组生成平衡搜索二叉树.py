class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def getTree(nums):
	if not nums:return None
	mid = int(len(nums)/2)
	root = TreeNode(nums[mid])
	root.left = getTree(nums[:mid])
	root.right = getTree(nums[mid+1:])
	return root 

def inOrderrec(root,result):
	if root:
		inOrderrec(root.left,result)
		result.append(root.val)
		inOrderrec(root.right,result)

a = [1,2,3,4,5,6,7,8,9]
b = getTree(a)
result = []
inOrderrec(b, result)
print(result)