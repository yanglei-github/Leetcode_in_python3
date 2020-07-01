# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:43:38 2020

@author: leiya
"""
#注意通过多设置维度，消除后效性
#0：not hold 1:hold 2:freeze
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #判断特例
        if len(prices) < 2: 
            return 0
        
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        
        
        for i in range(1, len(prices)): 
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])
            dp[i][2] = dp[i-1][0]
        return max(dp[-1][0], dp[-1][2])
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        l = len(prices)
        dp = [[0, 0] for _ in range(l+1)]
        dp[0][1] = float('-inf')
        dp[1][1] = -prices[0]
        for i in range(2, l+1): # 因为下面有i-2所以从2开始, 自行去填0-1的base case
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-1])
        return dp[-1][0]