# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
https://leetcode-cn.com/problems/balanced-binary-tree/
在计算深度的时候加个判断
'''
class Solution:
    def __init__(self):
        self.res = True
    def getheight(self, root):
        if not root:return 0
        left = self.getheight(root.left)
        right = self.getheight(root.right)
        if abs(left-right) > 1:
            self.res = False
        return max(left,right)+1
        
    def isBalanced(self, root: TreeNode) -> bool:
        self.getheight(root)
        return self.res
