# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 06:40:31 2020

@author: leiya
"""

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
    
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        
        stack, res = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return res


    