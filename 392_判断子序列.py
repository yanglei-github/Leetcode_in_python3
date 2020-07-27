# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:20:25 2020

@author: leiya
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = 0
        l2 = 0
        while l1 < len(s) and l2 < len(t):
            while l2 < len(t) and t[l2] != s[l1]:
                l2 += 1
            if l2 >= len(t):
                return False
            l1 += 1
            l2 += 1
        if l1 >= len(s):
            return True
        return False