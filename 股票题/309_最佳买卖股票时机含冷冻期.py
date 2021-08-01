# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:43:38 2020

@author: leiya
"""
#注意通过多设置维度，消除后效性
#0：not hold cash in hand after selling 1:hold 2:freeze
#注意判断特殊情况


'''
0710
dp[i][0] 表示第i天结束，处于可以买入的状态(即手中不持有股票)的收益的最大值     0->1->2;2->0
dp[i][1] 表示第i天结束，手中有股票的状态的收益的最大值
dp[i][2] 表示第i天结束，处于冷冻期的收益的最大值
0713
画出状态转换图更容易理解
0723
dp[i][0]容易写成dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices),问题在于前一天如果卖出了股票，那么当前天i的状态应该是2而不是0，
换句话说，也就是，只要在前一天卖了，第二天的状态直接变为2，即1->2,但是1->0是不成立的
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0,0,0] for _ in range(len(prices))]
        #一旦涉及到超过0的index，一定要先判断当前数据结构是否存在内容
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1][0],dp[-1][2])
    
    
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