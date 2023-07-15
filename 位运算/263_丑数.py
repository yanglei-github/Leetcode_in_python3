# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:26:14 2020

@author: leiya
"""

#判断特例：0不是丑数，1是丑数
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 5 == 0:
            num = num // 5
        while num % 3 == 0:
            num = num // 3
        while num % 2 == 0:
            num = num // 2
        if num == 1:
            return True
        else:
            return False