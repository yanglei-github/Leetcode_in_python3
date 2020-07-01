# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:16:14 2019

@author: leiya
"""

'''
updated: 0630
注意最后比较的是res和之前的值
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        newx = x
        while newx != 0:
            temp = newx % 10
            res = 10*res + temp
            newx = newx // 10
        return res == x
    
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        raw = x
        result = 0
        while x > 0:
            a = x % 10
            result = result * 10 + a
            x //= 10
        if result == raw:
            return True
        else:
            return False