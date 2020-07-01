# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:52:30 2020

@author: leiya
"""

class Solution:
    import math
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c**0.5)
        while i <= j:
            if i**2 + j**2 == c:
                return True
            elif i**2 + j**2 < c:
                i += 1
            else:
                j -= 1
        return False