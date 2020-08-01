# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:36:26 2020

@author: leiya
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = [root]
        res = []
        while queue:
            pop_node = queue.pop(0)
            if pop_node:
                res.append(str(pop_node.val))
                queue.append(pop_node.left)
                queue.append(pop_node.right)
            else:
                res.append('null')
        return '['+','.join(res)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        vals = data[1:-1].split(',')
        index = 1
        root = TreeNode(int(vals[0]))
        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            if vals[index] != 'null':
                pop_node.left = TreeNode(int(vals[index]))
                queue.append(pop_node.left)
            index += 1
            if vals[index] != 'null':
                pop_node.right = TreeNode(int(vals[index]))
                queue.append(pop_node.right)
            index += 1
        return root