# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:44:14 2020

@author: leiya
"""

'''
0909 
中序遍历当前从queue从弹出的pop_node.val一定比之前一个弹出来的node的val大，这保证了二叉搜索树的性质
'''
#节点的左子树只包含小于当前节点的数
#节点的右子树只包含大于当前节点的数，这意味着节点右子树中的所有节点都大于当前节点，即右子树中的左子树也要大于当前节点
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #if root is None:
            #return True
        #为了让第一次的pop_node可以顺利通过，temp要初始化一个无穷小
        temp = float('-inf')
        stack = []
        cur = root
        #除了层次遍历用queue，其他遍历均用stack，不要搞错了
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            pop_node = stack.pop()
            #此处应该有等于号
            if pop_node.val <= temp:
                return False
            else:
                temp = pop_node.val
            cur = pop_node.right
        return True
    
#递归形式
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True

        return helper(root)