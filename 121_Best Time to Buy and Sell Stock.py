# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:17:27 2020

@author: leiya
"""
#每一个状态是今天可以得到的最大利润，也就意味着今天也可以卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0 for _ in range(len(prices))]
        minprice = prices[0]
        for i in range(1, len(prices)):
            minprice = min(prices[i],minprice)
            dp[i] = max(dp[i-1],prices[i]-minprice)
        return dp[-1]
    
    
#动态规划的优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for i in prices:
            min_price = min(i, min_price)
            update_profit = i - min_price
            max_profit = max(max_profit, update_profit)
        return max_profit
    
    
#暴力法
def maxProfit(prices):
    res = []
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                res.append(prices[j]-prices[i])
    if res == []:
        return 0
    else:
        return max(res)

