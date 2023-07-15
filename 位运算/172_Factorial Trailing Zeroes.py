# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:26:23 2020

@author: leiya
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count
