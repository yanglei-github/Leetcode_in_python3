# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:30:26 2020

@author: leiya
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        adict = {}
        for i in range(len(s)):
            if s[i] not in adict:
                adict[s[i]] = 1
            else:
                adict[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in adict:
                return False
            else:
                if adict[t[j]] == 0:
                    return False
                else:
                    adict[t[j]] -= 1
        return True