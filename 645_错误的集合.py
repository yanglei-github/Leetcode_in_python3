# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:22:23 2020

@author: leiya
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        new_nums = nums + [i+1 for i in range(len(nums))]
        xor = 0
        for num in new_nums:
            xor ^= num
        bit = 1
        while xor & bit == 0:
            bit = bit << 1
        a = 0
        b = 0
        for num in new_nums:
            #千万注意此处只能和0比，因为不确定是哪一位可以与成1，such as  0000100这个与以后的结果不一定是1，但一定不是0，因此不能与1比
            if bit & num == 0:
                a ^= num
            else:
                b ^= num
        for num in nums:
            if a == num:
                return [a,b]
        return [b,a]