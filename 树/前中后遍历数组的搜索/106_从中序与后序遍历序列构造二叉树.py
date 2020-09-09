# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:03:47 2020

@author: leiya
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        #left + root = index+1个，那么在postorder中从零开始到index正好有index个left nodes
        left_node = self.buildTree(inorder[:index],postorder[:index])
        right_node = self.buildTree(inorder[index+1:],postorder[index:-1])
        root.left = left_node
        root.right = right_node
        return root