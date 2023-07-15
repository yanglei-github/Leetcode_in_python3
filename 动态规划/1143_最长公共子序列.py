# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:32:33 2020

@author: leiya
"""

#两个字符串的动态规划问题，联系72题，编辑距离
'''因为子序列类型的问题，穷举出所有可能的结果都不容易，而动态规划算法做的就是穷举 + 剪枝，
它俩天生一对儿。所以可以说只要涉及子序列问题，十有八九都需要动态规划来解决'''
#要设定dp的0,0位置为两个字符串都为空时候对应的最长公共子串
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        for i in range(1, row+1):
            for j in range(1, col+1):
                #dp[i][j]对应第i,j个字母,也就是字符串中index是i-1,j-1对应的字母
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

