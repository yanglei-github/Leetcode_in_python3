# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:34:54 2020

@author: leiya
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = 1
        count = 0
        for _ in range(32):
            if bit & n == 1:
                count += 1
            n >>= 1
        return count