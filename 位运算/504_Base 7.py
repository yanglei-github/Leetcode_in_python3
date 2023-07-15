# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:19:40 2020

@author: leiya
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        old_num = num
        num = abs(num)
        res = ''
        while num != 0:
            temp = num % 7
            num = num // 7
            res += str(temp)    
        if old_num < 0:
            return '-' + res[::-1]
        else:
            return res[::-1]