# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:40:16 2020

@author: leiya
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(path,k,depth,res,start,n):
            if depth == k:
                res.append(copy.deepcopy(path))
                return 

            for i in range(start,n+1):    
                path.append(i)
                dfs(path,k,depth+1,res,i+1,n)
                path.pop()
        res = []
        path = []
        depth = 0
        start = 1
        dfs(path,k,depth,res,start,n)
        return res