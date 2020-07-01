# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:34:49 2020

@author: leiya
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        adic = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ''
        if num < 0:
            num = num + 16**8
            #16**8=4,294,967,296
        while num != 0:
            temp = num % 16
            num = num // 16
            if temp >= 10:
                res += adic[temp]
            else:
                res += str(temp)
        return res[::-1]