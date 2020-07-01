# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:16:58 2019

@author: leiya
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        adic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = adic[s[0]]
        for i in range(1,len(s)):
            if adic[s[i]] <= adic[s[i-1]]:
                res = res + adic[s[i]]
            else:
                res = res - 2*adic[s[i-1]] + adic[s[i]]
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
                result += numeral_map[s[i]] - 2 * numeral_map[s[i-1]]
            else:
                result += numeral_map[s[i]]
        return result

class Solution:
    def romanToInt(self, s: str) -> int:
        amap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = amap[s[0]]
        for i in range(1,len(s)):
            if amap[s[i]] <= amap[s[i-1]]:
                result += amap[s[i]]
            else:
                result += amap[s[i]] - 2 * amap[s[i-1]]
        return result