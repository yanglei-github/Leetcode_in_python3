# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:33:06 2020

@author: leiya
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ''
        res = ''
        while n != 0:
            n = n -1
            temp = n % 26
            n = n // 26 
            res += chr(temp+65)
        return res[::-1]