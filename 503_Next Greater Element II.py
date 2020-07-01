# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:30:52 2020

@author: leiya
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [-1] * length
        stack = []
        for i in range(length*2):
            index = i % length
            while stack and nums[index] > nums[stack[-1]]:
                res[stack.pop()] = nums[index]
            stack.append(index)
        return res
