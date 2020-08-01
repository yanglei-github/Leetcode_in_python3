# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:31:04 2020

@author: leiya
"""


'''
0730
树与回溯
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
                #path.append(root.val)
                res.append(path[:])
                return
            
            dfs(root.left,path + [root.val], sum - root.val)
            dfs(root.right,path + [root.val], sum - root.val)
            
            

        dfs(root, path, sum)
        return res

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(root,path,sum):
            if not root: 
                return 
            
            if not root.left and not root.right and root.val == sum:  
                path.append(root.val)
                res.append(path[:])
                path.pop()
                return
            #联想全排列
            '''
            for i in range(len(nums)):
                path.append()
                dfs()
                path.pop()
            '''
            path.append(root.val)
            dfs(root.left,path, sum - root.val)
            path.pop()
            path.append(root.val)
            dfs(root.right,path, sum - root.val)
            path.pop()
            
        dfs(root, path, sum)
        return res
    
    
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        def dfs(root, path, sum):
            if root.left is None and root.right is None:
                if sum == 0:
                    res.append(path[:])
                return 
                
            if root.left:
                dfs(root.left, path+[root.left.val], sum-root.left.val)
                
            if root.right:
                dfs(root.right, path+[root.right.val], sum-root.right.val)
                
        dfs(root, [root.val], sum-root.val)
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

