# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 08:08:23 2020

@author: leiya
"""

'''
inorder.index(preorder[0]) 这一步获取根的索引值，
题目说树中的各个节点的值都不相同，也确保了这步得到的结果是唯一准确的。
而且这个idx还能当长度用相当于 左+根 的长度，因为 左+根 和 根+左 是等长的。

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        #分别在preorder和inorder中找到符合要求的所有左子树节点和右子树节点，作为完整的树传入下一次递归中
        left_node = self.buildTree(preorder[1:1+index],inorder[:index])
        right_node = self.buildTree(preorder[1+index:],inorder[index+1:])
        root.left = left_node
        root.right = right_node
        return root