# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:20:05 2020

@author: leiya
"""

 """
 （1）思路：动态规划
 我们以dp[i][j]表示区间[i, j]之间的子串是否为回文子串，这样可以思考这样三种情况的回文子串：
 - 子串长度为1，例如 a 一定为回文子串，即 i=j 的情况
 - 子串长度为2，且字符相同，例如 aa 一定为回文自传，即 s[i] = s[j] and j-i = 1
 - 子串长度大于2，符合 abcba 形式的为回文子串，根据回文子串的定义，那么 abcba 去掉两边字符，仍为回文
 子串，即bcb，转换成方程形式即 dp[i][j] = dp[i+1][j-1] and j-i > 1 and s[i] = s[j]
 剩下的均为不符合条件，即非回文子串。

（2）复杂度：
- 时间复杂度：O（N^2）
- 空间复杂度：O（N^2）
"""

#updated 0630 基本和5一样的思路,就是判断回文的个数是基于判断各种情况下是否是回文，5是判断所有回文中最长的那个，都是dp之后的变体
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        count = 0
        for i in range(size):
            dp[i][i] = True
            count += 1
        for j in range(1,size):
            for i in range(j):
                if s[i] == s[j] and j-i==1:
                    dp[i][j] = True
                    count += 1
                elif s[i] == s[j] and j-i > 1:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j]:
                        count += 1
        return count
    
