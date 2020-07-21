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

'''
0721
dfs的意义是能不能在当前给定的root代表的树中找到一组路径和为sum，这个模型最终重复到只有一个root的时候，如果只有一个root的时候不满足sum，那么就不对
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(root,sum):
            if not root:
                return False
            '''
            注意符合要求的条件在于该node的左右都没有node了（意味着它是叶子节点，不加这个判断没办法确定是叶子节点）且他的值为sum
            '''
            if not root.left and not root.right and root.val == sum:
                return True
            else:
                return dfs(root.left,sum-root.val) or dfs(root.right,sum-root.val)
                
        if dfs(root,sum):
            return True
        else:
            return False
        
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum-root.val)
        