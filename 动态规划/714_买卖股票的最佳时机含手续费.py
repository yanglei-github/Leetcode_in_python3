# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:48:50 2020

@author: leiya
"""


'''
0713
统一了121,122,309,714的状态定义以及模板
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        #默认每次买入的时候收手续费，也可以写成每次卖出的时候收手续费，这里买入要花一笔钱，索性就一起花了
        dp[0][1] = -prices[0] - fee
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i]-fee)
        return dp[-1][0]
    
    
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)

        if size < 2:
            return 0

        # dp[i][j] 表示 [0, i] 区间内，到第 i 天（从 0 开始）状态为 j 时的最大收益
        # j = 0 表示不持股，j = 1 表示持股
        # 并且规定在买入股票的时候，扣除手续费

        dp = [[0, 0] for _ in range(size)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee

        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[-1][0]