# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def getseries(root):
            if not root:
                return ''
            return str(root.val)+getseries(root.left)+getseries(root.right)
        s1 = getseries(pRoot1)
        s2 = getseries(pRoot2)
        return s2 in s1 if s2 else False 


'''
参考https://github.com/imhuay/Algorithm_Interview_Notes-Chinese/blob/master/C-%E7%AE%97%E6%B3%95/%E4%B8%93%E9%A2%98-A-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md#%E5%88%A4%E6%96%AD%E6%A0%91-b-%E6%98%AF%E5%90%A6%E4%B8%BA%E6%A0%91-a-%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84
用递归来写
class Solution {
public:
    bool HasSubtree(TreeNode* p1, TreeNode* p2) {
        if (p1 == nullptr || p2 == nullptr)  // 约定空树不是任意一个树的子结构
            return false;
        
        return isSubTree(p1, p2)    // 判断子结构是否相同
            || HasSubtree(p1->left, p2)      // 递归寻找树 A 中与树 B 根节点相同的子节点
            || HasSubtree(p1->right, p2);
    }
    
    bool isSubTree(TreeNode* p1, TreeNode* p2) {
        if (p2 == nullptr) return true;        // 注意这两个判断的顺序
        if (p1 == nullptr) return false;
        
        if (p1->val == p2->val)
            return isSubTree(p1->left, p2->left)    // 递归判断左右子树
                && isSubTree(p1->right, p2->right);
        else
            return false;
    }
};
'''