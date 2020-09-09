# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:31:14 2020

@author: leiya
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
    

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]

