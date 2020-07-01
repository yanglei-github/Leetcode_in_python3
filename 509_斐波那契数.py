# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:27:21 2020

@author: leiya
"""


class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        dp = [0 for _ in range(N+1)]
        dp[1] = 1
        for i in range(2,N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    

class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        onestep = 1
        twostep = 0
        for i in range(2,N+1):
            twostep, onestep = onestep, onestep + twostep 
        return onestep