'''
这里求得是每层最右边节点的位置-最左边节点的位置
https://leetcode-cn.com/problems/maximum-width-of-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:return 0
        stack = []
        if root.left:stack.append((root.left,1))
        if root.right:stack.append((root.right,2))
        res = 1
        while stack:
            res = max(res,stack[-1][1]-stack[0][1]+1)
            for i in range(len(stack)):
                t = stack.pop(0)
                if t[0].left:stack.append((t[0].left,2*t[1]+1))
                if t[0].right:stack.append((t[0].right,2*(t[1]+1)))
        return res
        