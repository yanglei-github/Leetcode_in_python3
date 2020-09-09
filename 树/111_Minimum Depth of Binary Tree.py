# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:24:51 2020

@author: leiya
"""

'''
0909
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            return max(left_depth, right_depth) + 1
        else:
            return min(left_depth, right_depth) + 1
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        '''
        难点在于如果当前传入的root左右根中有一个不存在一个存在，那么以当前root为树的最小深度实际上是左右子树中最大的那个，这一点有些反常识
        '''
        if root.left is not None and root.right is not None:
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left),self.minDepth(root.right)) + 1