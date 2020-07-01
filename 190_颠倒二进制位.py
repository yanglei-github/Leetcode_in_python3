# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:54:03 2020

@author: leiya
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res, power = 0, 31
        while n:
            #判断当前位是0是1，然后移动到power处
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res