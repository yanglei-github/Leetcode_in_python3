# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:19:26 2020

@author: leiya
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        length = len(s)
        max_length = 1
        current_index = 0
        dp = [[False for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        for j in range(1,length):
            for i in range(j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j]:
                    current_length = j - i + 1
                    if current_length > max_length:
                        max_length = current_length
                        current_index = i 
        return s[current_index:current_index+max_length]
    
    
#注意max_len的初始化要初始化成1，因为最坏的结果也是有一个单独字母构成回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        
        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]