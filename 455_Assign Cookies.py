# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:07:08 2020

@author: leiya
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g = sorted(g)
        s = sorted(s)
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1   
        return count