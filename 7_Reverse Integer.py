# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:18:32 2019

@author: leiya
"""

'''
0630 updated
'''
class Solution:
    def reverse(self, x: int) -> int:
        newx = abs(x)
        reversex = 0
        while newx != 0:
            temp = newx % 10
            reversex = 10 * reversex + temp
            newx = newx // 10
        if x < 0:
            if -2**31 <= -reversex:

                return -reversex
            else:
                return 0
        else:
            if reversex <= 2**31 -1:
                return reversex
            else:
                return 0
            
class Solution:
    def reverse(self, x):
        #-2147483648-2147483647
        a = abs(x)
        num = 0
        while a != 0:
            temp = a % 10
            num = num*10 + temp
            a = int(a / 10)
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else: 
            return 0

class Solution:
    def reverse(self, x):
        #反转完了以后也不能超出范围
        if x >= 0 and x <= 2**31 - 1:
            if int(str(x)[::-1]) > 2**31 - 1:
                return 0
            else:
                return int(str(x)[::-1])
        elif x < 0 and x >= -2**31:
            if -int(str(x)[1:][::-1]) < -2**31:
                return 0
            else:
                return -int(str(x)[1:][::-1])
        else:
            return 0

class Solution:
    def reverse(self, x):
        #-2147483648-2147483647
        result = 0
        m = abs(x)
        while m > 0:
            a = m % 10
            result = result * 10 + a
            m //= 10
        if x < 0 and -2**31 <= -result:
            return -result
        elif 0 < x and result <= 2**31-1:
            return result
        else:
            return 0     