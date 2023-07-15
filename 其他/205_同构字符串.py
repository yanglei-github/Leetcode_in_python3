# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:52:29 2020

@author: leiya
"""

#记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        adict = {}
        bdict = {}
        for i in range(len(s)):
            if s[i] not in adict and t[i] not in bdict:
                adict[s[i]] = i
                bdict[t[i]] = i
            elif s[i] not in adict and t[i] in bdict:
                return False
            elif s[i] in adict and t[i] not in bdict:
                return False
            
            else:
                if adict[s[i]] != bdict[t[i]]:
                    return False
        return True