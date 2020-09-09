# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:30:53 2020

@author: leiya
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            pop_node = stack.pop()
            res.append(pop_node.val)
            cur = pop_node.right
        return res
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            pop_node = stack.pop()
            res.append(pop_node.val)
            cur = pop_node.right
        return res
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res