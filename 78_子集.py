# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:40:54 2020

@author: leiya
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #判断解空间变化情况：不重复，与顺序无关，因此无须使用used
        def dfs(nums,res,path,start_index):
            res.append(path[:])
            #这段判断没有实际效果，但是为了便于理解可以加上
            if start_index == len(nums):
                return
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                dfs(nums,res,path,i+1)
                path.pop()
        res = []
        path = []
        start_index = 0
        dfs(nums,res,path,start_index)
        return res
    
    
#线性缩小解空间，可以引入start_index
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,path,res,start):
            '''
            start == len(nums)的时候直接返回了
            '''
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(nums,path,res,i+1)
                path.pop()
        res = []
        path = []
        start = 0
        dfs(nums,path,res,start)
        return res