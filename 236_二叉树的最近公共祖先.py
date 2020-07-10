# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:35:50 2020

@author: leiya
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root is q or root is p:
            return root
        #最高层面上来看的话left中包含的是在root的左子树中p,q存在的最深层的公共祖先，也可能返回的就是p,q中一个node所在的位置，
        #因为p,q可能在不同子树中
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None
        elif not left and right:
            return right
        elif left and not right:
            return left
        else:
            return root