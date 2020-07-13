# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:46:00 2019

@author: leiya
"""

'''
0712
滑动窗口
这道题的升级版是567,只要needle中的元素全在窗口中就行，可以打乱重组，需要用hashmap去比较
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #定长滑动窗口
        start = 0
        for end in range(len(needle)-1,len(haystack)):
            if haystack[start:end+1] == needle:
                return start
            start += 1
        return -1
    
#------------------------------------------------------------
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
        

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        

