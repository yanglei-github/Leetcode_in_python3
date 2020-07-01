# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:40:54 2020

@author: leiya
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,path,res,start):
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