# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:41:17 2020

@author: leiya
"""

#在判断回文串的基础上
class Solution:
    def validPalindrome(self, s: str) -> bool:

        if not s:
            return True
        low = 0
        high = len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.isPalindrome(s,low+1,high) or self.isPalindrome(s,low,high-1)
        return True
    def isPalindrome(self,s,low,high):
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False
        return True
#会有这种特殊情况的出现: lcuppucul
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.isPalindrome(s,i+1,j) or self.isPalindrome(s,i,j-1)
        return True
    
    def isPalindrome(self, s, head, tail):
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                return False
        return True

#不用函数封装的话时间复杂度太高
def validPalindrome(s):
    flag = 0
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            ii = i
            jj = j
            while i < j:
                if s[i+1] == s[j]:
                    i += 1
                    j -= 1
                else:
                    flag = 1
            if flag == 0:
                return True
            else:
                while ii < jj:
                    if s[i] == s[j-1]:
                        i += 1
                        j -= 1
                    else:
                        return False
        return True
print(validPalindrome('acbddca'))