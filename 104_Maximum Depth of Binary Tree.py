# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:26:08 2019

@author: leiya
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
      
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        

#updated: 0628
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            current_len = len(queue)
            count += 1
            for _ in range(current_len):
                pop_node = queue.pop(0)
                if pop_node.left is not None:
                    queue.append(pop_node.left)
                if pop_node.right is not None:
                    queue.append(pop_node.right)
        return count
       
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        cur_queue = [root]
        count = 0
        while cur_queue:
            next_queue = []
            for node in cur_queue:
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)
                
            count += 1
            cur_queue = next_queue
        return count