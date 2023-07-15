# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:49:29 2020

@author: leiya
"""

'''
任何数和 0 做异或运算，结果仍然是原来的数。
任何数和其自身做异或运算，结果是 0
异或运算满足交换律和结合律
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
    
    
#把list中所有元素异或一遍，这样相同元素异或变成零，零和最后一个单独的数异或得到单独的这个数的值
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        adict = {}
        for num in nums:
            if num not in adict:
                adict[num] = 1
            else:
                adict[num] += 1
        for word in adict.keys():
            if adict[word] == 1:
                return word