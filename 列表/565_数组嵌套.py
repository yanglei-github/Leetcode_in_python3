# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:10:15 2020

@author: leiya
"""

#brute force, 超时
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 1
        for i in range(len(nums)):
            memory = [i]
            length = 1
            while nums[i] not in memory:
                i = nums[i]
                memory.append(i)
                length += 1
            max_length = max(max_length,length)
        return max_length
    

#注意剪枝
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            d[i] = nums[i]
        count = 0
        i = 0
        while i < len(nums):
            tmp = i
            ans = 0
            while d[tmp] != '#':
                ans += 1
                res = d[tmp]
                d[tmp] = '#'
                tmp = res
            i += 1
            count = max(count,ans)
        return count