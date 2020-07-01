# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:28:29 2020

@author: leiya
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum-root.val)
        