class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None 
'''
1.有右子树，后继就是右子树的最左节点
2.没有右子树，如果是左儿子，后继就是它爸爸
3.没有右子树，且是右儿子，就一直上找到第一个是左儿子的爸爸

'''

def getNextNode(node):
    if not node:return 
    if node.right:
        t = node.right 
        while t:
            t = t.left 
        return t 
    else:
        parent = node.parent
        while parent and node != parent.left:
            node = node.parent
            parent = node.parent
        return parent
        