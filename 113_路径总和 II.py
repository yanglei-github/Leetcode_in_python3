# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:31:04 2020

@author: leiya
"""


'''
其实涉及树的回溯不用写出明确的回溯三步
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(root,path,sum):
            if not root: 
                return 
            
            if not root.left and not root.right and root.val == sum:
                path += [root.val]
                res.append(path[:])
            
            dfs(root.left,path + [root.val], sum - root.val)
            dfs(root.right,path + [root.val], sum - root.val)
            
            

        dfs(root, path, sum)
        return res
    
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res 
        
        def dfs(root, path, sum):
            if root.left is None and root.right is None:
                if sum == 0:
                    res.append(path[:])
                return 
                
            if root.left:
                path.append(root.left.val)
                dfs(root.left, path, sum-root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, path, sum-root.right.val)
                path.pop()
            
        
        dfs(root, [root.val], sum-root.val)
        return res 

