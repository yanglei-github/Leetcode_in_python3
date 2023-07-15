# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:55:49 2020

@author: leiya
"""

#结合645题
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor 为特殊两个数的异或
        xor = 0
        for num in nums:
            xor = xor ^ num
        # bit 为xor 第一个为1的位
        bit = 1
        while xor & bit == 0:
            bit <<= 1
            #bit = bit << 1
            #bit = bit * 2右移
        # 通过和bit异或的结果，把数分为两组，两个数肯定在不同组，两个组异或出的结果就是两个数
        a = 0
        b = 0
        for num in nums:
            #bit其他位均为0，只有一位是1，这意味就是两个数不同的一位，这样，如果有数在这位也是1那么就可以得到1
            if num & bit == 0:
                a ^= num
            else:
                b ^= num
        return [b,a]
    
        
