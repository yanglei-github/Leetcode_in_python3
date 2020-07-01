# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:46:00 2019

@author: leiya
"""
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
        

