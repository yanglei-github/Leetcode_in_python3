# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:05:49 2020

@author: leiya
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        for i in range(len(nums)):
            if target - nums[i] in adict:
                return [adict[target - nums[i]],i]
            else:
                adict[nums[i]] = i