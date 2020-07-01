# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:35:50 2020

@author: leiya
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root is q or root is p:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        elif not left and right:
            return right
        elif left and not right:
            return left
        else:
            return root