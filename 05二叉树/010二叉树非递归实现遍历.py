class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


#前序遍历
def preOrderrec(root,result):
	if root:
		result.append(root.val)
		preOrderrec(root.left,result)
		preOrderrec(root.right,result)
	

def preOrder(root):
	if not root:return 
	stack = []
	stack.append(root)
	res = []
	while stack:
		t = stack.pop()
		res.append(t.val)
		if t.right:stack.append(t.right)
		if t.left:stack.append(t.left)
	return res 

#中序遍历
def inOrder(root):
	if not root:return 
	stack = []
	res = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left 
		else:
			t = stack.pop()
			res.append(t.val)
			if t.right:
				root = t.right
	return res
def inOrderrec(root,result):
	if root:
		inOrderrec(root.left,result)
		result.append(root.val)
		inOrderrec(root.right,result)

#后续遍历: 用两个栈，可以看成是先做一次前序，然后取出来,根左右 vs左右根，可以用两个栈反过来
def posOrderrec(root, result):
	if root:
		posOrderrec(root.left,result)
		posOrderrec(root.right,result)
		result.append(root.val)

def posOrder(root):
	if not root:return 
	stack1 = []
	stack2 = []
	res = [] 
	stack1.append(root)
	while stack1:
		t = stack1.pop()
		stack2.append(t.val)
		if t.left:stack1.append(t.left)
		if t.right:stack1.append(t.right)
		
	while stack2:
		res.append(stack2.pop())
	return res 

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
#result = []
#preOrderrec(head,result)
#print(result)
#print(preOrder(head))
#result = []
#inOrderrec(head,result)
#print(result)
#print(inOrder(head))
result = []
posOrderrec(head,result)
print(result)
print(posOrder(head))