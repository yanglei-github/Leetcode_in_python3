# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:17:27 2020

@author: leiya
"""

'''
0723：最好将状态理解为股票的持有状态，而不要理解为买卖，这样容易导致我们认为状态1一定要在今天买，实际上状态1的意义是，今天手里有股票，可以是今天现买的，
也可以是之前某一天买的，之后已知没动过，对于状态的精确理解对于这道题十分重要，另外需要补充的是dp[i]表示前i天直到今天最大的理论，而不是当前天最大利润，
当前天最大利润是没有实际意义的

0713
0:cash in hand after selling stock   1:hold stock
dp[i][1] = max(dp[i-1][1],-prices[i])很容易写成max(dp[i-1][1],dp[i-1][0]-prices[i])
后者意义是前一天cash在手，今天买股票，理论上自然会想成前一天cash在手的最大利润减去prices[i]就是今天最大利润
但是这道题的前提是只能买卖一次，也就是说如果选择今天卖出的话，那么是不存在前一天cash在手的最大利润这个概念的，因为前面还没有买卖过stock，因为今天刚买
因此后者正好可以用来计算可以买卖无数次的情况，这样dp[i-1][0]-prices[i]就有意义了，因为前一天cash在手也可能有利润，可能是前面某天买卖的股票赚了一笔
更进一步的话，我们可以更精确的定义dp[i][0]的含义为之前卖了或者今天卖了的最大利润，dp[i][1]为之前买了或者，之前从来没买过今天第一次买，这两种情况中的最大值
这样dp[i-1][0]-prices[i]就没有意义了，因为dp[i-1][0]无论是哪种情况都表明已经完成了唯一的一次股票交易，今天不可能再进行股票交易了

另外由于用到prices[0]，需要一开始对prices判断特殊情况
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]
    
    
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

