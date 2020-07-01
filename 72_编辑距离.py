# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:48:55 2020

@author: leiya
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for j in range(1, len(word2)+1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, len(word1)+1):
            dp[i][0] = dp[i-1][0] + 1
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]