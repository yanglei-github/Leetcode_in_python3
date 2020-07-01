# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:59:52 2020

@author: leiya
"""

#因为树是有指定路径顺序，回退操作有指针自行完成，不需要认为选取，这是和普通回溯法的区别
class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root:                    #当前节点存在
                path += str(root.val)   #当前节点的值加入路径中
                if not root.left and not root.right:    #叶子节点，将路径加入返回值
                    res.append(path)
                else:
                    path += '->'       #非叶子节点，继续递归添加
                    dfs(root.left, path)
                    dfs(root.right, path)
        res = []
        dfs(root, '')
        return res