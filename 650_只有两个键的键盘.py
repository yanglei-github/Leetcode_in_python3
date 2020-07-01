# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:06:43 2020

@author: leiya
"""

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(2, n+1):
            dp[i] = i
            #此循环在判断i是否为质数
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    break              
        return dp[-1]