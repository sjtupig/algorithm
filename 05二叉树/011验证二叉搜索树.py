# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
leetcode
https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/
'''
import math
class Solution:
    def __init__(self):
        self.last = -math.inf
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:return True
        if self.isValidBST(root.left):
            if self.last < root.val:
                self.last = root.val
                return self.isValidBST(root.right)
        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)
        inorder(root,result)
        t = True
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                t = False
        return t