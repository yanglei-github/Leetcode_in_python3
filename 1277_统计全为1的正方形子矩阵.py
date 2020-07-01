# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:10:11 2020

@author: leiya
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

                    count += dp[i][j]
        return count