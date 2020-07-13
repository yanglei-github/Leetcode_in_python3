# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:37:28 2020

@author: leiya
"""


'''
0713
与121唯一不同在于dp[i][1]的更新策略，本质在于dp[i][0]的含义是在i及i天之前某个时刻卖出stock后手里有cash,无stock的最大利润
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        #注意从1开始
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
    
    
#动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


#贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                price += prices[i] - prices[i-1]
        return price
            