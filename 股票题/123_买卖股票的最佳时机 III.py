# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:45:31 2020

@author: leiya
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0,0,0,0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        #因为在更新dp[i][2]的时候可能会出现比0小的数，因为dp[i-1][1]-prices[i]
        #所以这个时候dp[i][2]不能默认是0，相反dp[i][3]就可以默认是0
        #dp[0][1]不需要更新是因为第一次卖出的时候一定式prices[i] > dp[i-1][0]才会卖出
        dp[0][2] = float('-inf')
        

        # dp[j]：i 表示 [0, i] 区间里，状态为 j 的最大收益
        # j = 0：什么都不操作，没有意义，不会更新最大利润
        # j = 1：第 1 次买入一支股票
        # j = 2：第 1 次卖出一支股票
        # j = 3：第 2 次买入一支股票
        # j = 4：第 2 次卖出一支股票

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + prices[i])
        return max(dp[-1][1], dp[-1][3])
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0,0,0,0,0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        dp[0][3] = float('-inf')
        dp[0][4] = float('-inf')

        # dp[j]：i 表示 [0, i] 区间里，状态为 j 的最大收益
        # j = 0：什么都不操作
        # j = 1：第 1 次买入一支股票
        # j = 2：第 1 次卖出一支股票
        # j = 3：第 2 次买入一支股票
        # j = 4：第 2 次卖出一支股票

        for i in range(1, len(prices)):
            dp[i][0] = 0
            dp[i][1] = max(dp[i-1][1], - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        return max(0, dp[-1][2], dp[-1][4])