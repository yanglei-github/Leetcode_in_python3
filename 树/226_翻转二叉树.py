# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:57:52 2020

@author: leiya
"""

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    
#层次遍历+交换左右节点
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)
            pop_node.left, pop_node.right = pop_node.right, pop_node.left

        return root
    

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            pop_node.left, pop_node.right = pop_node.right, pop_node.left
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)
            

        return root