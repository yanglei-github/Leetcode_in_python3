# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:26:15 2020

@author: leiya
"""
#方法一：直接动态规划
#方法二：只需要求出最公共长子序列（1143题），然后算出总字符串长度，减去二倍的子序列长度

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(1, len(word1)+1):
            dp[i][0] = dp[i-1][0] + 1
        for j in range(1, len(word2)+1):
            dp[0][j] = dp[0][j-1] + 1

        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1) + 1
                    #dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1]
