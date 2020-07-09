# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:55:35 2020

@author: leiya
"""

'''
0705
写while循环的时候一定要手动更新while循环的条件，要不然很容易造成死循环
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            if i < 0:
                a = 0
            else:
                a = num1[i]
            if j < 0:
                b = 0
            else:
                b = num2[j]
                
            temp = int(a) + int(b) + carry
            carry = temp // 10
            res += str(temp % 10)
            i -= 1
            j -= 1
        #注意加完了以后要颠倒一下
        return res[::-1]