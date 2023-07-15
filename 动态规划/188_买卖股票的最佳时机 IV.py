# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:15:02 2020

@author: leiya
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        if size < 2 or k == 0:
            return 0
        if k >= size // 2:
            res = 0
            for i in range(1, size):
                if prices[i] > prices[i - 1]:
                    res += (prices[i] - prices[i - 1])
            return res
        #初始化：把持股的部分都设置为一个较大的负值
        dp = [[[0, float('-inf')] for _ in range(k + 1)] for _ in range(size + 1)]
        
        for i in range(1, size + 1):
            for j in range(1, k + 1):
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])

        return dp[size][k][0]
    
    
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        if size < 2 or k == 0:
            return 0
        if k >= size // 2:
            res = 0
            for i in range(1, size):
                if prices[i] > prices[i - 1]:
                    res += (prices[i] - prices[i - 1])
            return res
        #初始化：把持股的部分都设置为一个较大的负值
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(size + 1)]
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                dp[0][j][1] = float('-inf')
            break
        for i in range(1, size + 1):
            for j in range(1, k + 1):
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])

        return dp[size][k][0]
    
