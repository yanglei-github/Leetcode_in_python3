# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:37:28 2020

@author: leiya
"""
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
            