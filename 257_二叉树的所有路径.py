# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:59:52 2020

@author: leiya
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        


#遍历出所有二叉树的路径
    def binaryTreePaths(self, root: TreeNode):
        #明显dfs
        def dfs(root,path):
            if not root:
                return []
            path += str(root.val)
            #print('3',path)
            if not root.left and not root.right:
                res.append(path)
            else:
                #每次进入到一个新的递归层中path就重新用了一个地址，已经不是之前的path了，
                #因此在该层中如何改变path,都不会影响上一层path的值，这一点需要特别和回溯法区分开
                path += '->'
                #print('1',id(path))
                dfs(root.left,path)
                #print('2',id(path))
                dfs(root.right,path)
        res = []
        dfs(root,'')
        return res
    
#因为树是有指定路径顺序，回退操作由指针自行完成，不需要人为选取，这是和普通回溯法的区别
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        #明显dfs
        def dfs(root,path):
            if not root:
                return []
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
            else:
                path += '->'
                print('1',path)
                dfs(root.left,path)
                print('2',path)
                dfs(root.right,path)
        res = []
        dfs(root,'')
        return res

solution = Solution()
res = solution.binaryTreePaths()
print(res)