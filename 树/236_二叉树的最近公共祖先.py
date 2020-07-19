# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:35:50 2020

@author: leiya
"""

'''
0719:统一模板
递归理解：在最高层上，我们需要判断root.left,root.right是否可以找到p,q，如果都找到则结果为root，反之需要分类处理
我们希望函数返回的是当前树的最近公共祖先
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left_node = self.lowestCommonAncestor(root.left,p,q)
        right_node = self.lowestCommonAncestor(root.right,p,q)
        if not left_node and not right_node:
            return None
        if left_node and not right_node:
            return left_node
        if not left_node and right_node:
            return right_node
        if left_node and right_node:
            return root
        
        
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