# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:11:52 2020

@author: leiya
"""


class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor % 2 == 1:
                distance += 1
            xor = xor >> 1
            #逻辑右移，即二进制形式向右移动一位，左边补零
            #xor = xor // 2
        return distance