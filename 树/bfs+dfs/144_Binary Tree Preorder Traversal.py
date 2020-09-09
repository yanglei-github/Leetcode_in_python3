# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 06:40:31 2020

@author: leiya
"""

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            pop_node = stack.pop()
            res.append(pop_node.val)
            if pop_node.right:
                stack.append(pop_node.right)
            if pop_node.left:
                stack.append(pop_node.left)
        return res
    
#由于在原有函数上直接写递归容易出现错误，所以最好单独写递归函数
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if root is None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root) 
        return res
    
、


    