# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:46:43 2020

@author: leiya
"""


'''
0712
凡是剪枝问题，一开始就把nums从小到大排序，这一点非常容易忘记
'''
#注意此时输入的nums无须且有重复数字，这意味着可能会搜索到相同的结果
#存在重复数字可能搜索到相同结果哦的情况下，首先将nums排序，之后再本层内判断是否有相同nums[i]，如果有则跳过
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(nums,path,res,start):
            res.append(path[:]) 
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums,path,res,i+1)
                path.pop()
        res = []
        path = []
        start = 0
        dfs(nums,path,res,start)
        return res