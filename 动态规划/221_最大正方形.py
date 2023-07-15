# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:47:27 2020

@author: leiya
"""
#矩阵中的的数据是string类型而非int类型
#dp[i][j]状态指[i,j]为右下角可以产生的最大正方形
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxedge = 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    maxedge = max(maxedge, dp[i][j])
        return maxedge ** 2