# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:16:15 2019

@author: leiya
"""

'''
0909
这道题的难点在于找最大深度的时候，不是单纯的找到root的左子树和右子树的最大深度比较一次就可以，
而是要对于所有root的左右子树都进行比较，这就要求，每深入一次递归，都要尽心最大深度的比较
'''
#updated 0628:在104基础上扩展，首先需要了解如何用递归找到一棵树的depth
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1
    
    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(root):
            if root is None:
                return 0
            left_height,right_height = get_height(root.left),get_height(root.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return (get_height(root) >= 0)