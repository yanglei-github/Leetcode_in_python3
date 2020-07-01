# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:55:59 2020

@author: leiya
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans, status, n = 0, 0, len(s)
        pos = [-1] * (1 << 5)
        #全为偶数时置为0
        pos[0] = 0

        for i in range(n):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            if pos[status] != -1:
                ans = max(ans, i + 1 - pos[status])
            else:
                pos[status] = i + 1
        return ans