# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:13:15 2020

@author: leiya
"""
#注意用dp时候先给dp声明空间
#注意迭代公式里还有上步更新的dp值
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i != 0 and j != 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                elif i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        return dp[-1][-1]