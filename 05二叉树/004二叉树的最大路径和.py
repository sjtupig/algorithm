# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/comments/
        对于任意一个节点, 如果最大和路径包含该节点, 那么只可能是两种情况:
        1. 其左右子树中所构成的和路径值较大的那个加上该节点的值后向父节点回溯构成最大路径
        2. 左右子树都在最大路径中, 加上该节点的值构成了最终的最大路径
        
'''
import math
class Solution:
    def __init__(self):
        self.maxv = -math.inf
        
    def p(self, root):
        if not root:return 0
        leftsum = max(self.p(root.left),0)
        rightsum = max(self.p(root.right),0)
        self.maxv = max(self.maxv,root.val+leftsum+rightsum)
        return max(leftsum,rightsum)+root.val
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.p(root)
        return self.maxv
        
        