# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:01:44 2020

@author: leiya
"""


#主要需要注意的问题在于，如果最后一个数恰好为1，那么其实最后一次循环的时候不可能进入else判断中，也就没办法把最后一步1的个数放入length中
#因此需要特殊处理这个问题
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                length = max(length,count)
            else:
                length = max(length,count)
                count = 0     
            
        return length


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                
            else:
                length = max(length,count)
                count = 0 
        return max(length,count)