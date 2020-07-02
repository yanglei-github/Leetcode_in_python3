# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 08:45:10 2020

@author: leiya
"""

'''
0702 形参过多，形参顺序不要传错位
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #无重复数组且解中无重复数字
        start_index = 1
        def dfs(k,n,res,path,start_index):
            if k == 0 and n == 0:
                res.append(path[:])
                return 
            for i in range(start_index,10):
                if i <= n:
                    path.append(i)
                    dfs(k-1,n-i,res,path,i+1)
                    path.pop()
        path = []
        res = []
        dfs(k,n,res,path,start_index)
        return res
    

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        start_index = 1
        def dfs(start_index,k,n,path,res):
            if n == 0 and k == 0:
                res.append(path[:])
                return
            if (n == 0 and k != 0) or (n != 0 and k == 0):
                return
            for i in range(start_index,10):
                if i <= n:
                    path.append(i)
                    dfs(i+1,k-1,n-i,path,res)
                    path.pop()
        path = []
        res = []
        dfs(start_index,k,n,path,res)
        return res

