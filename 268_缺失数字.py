# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:19:46 2020

@author: leiya
"""

#下标和value异或，初始值置为nums长度
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing