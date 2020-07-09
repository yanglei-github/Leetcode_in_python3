# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:20:08 2020

@author: leiya
"""


'''
0706
'''
#精简版
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
      
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 1
        return dp[-1][-1]
    
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
      
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                elif i == 0 or j == 0:
                    dp[i][j] = 1
        return dp[-1][-1]