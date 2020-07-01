# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:26:06 2019

@author: leiya

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        #没有台阶时候算有一种走法
        if n == 0:
            return 1
        if n == 1 or n == 2:
            return n
        dp_i_1 = 2
        dp_i_2 = 1
        for i in range(2, n):
            dp_i = dp_i_1 + dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
            
        return dp_i_1
#明确dp每个位置上的状态定义
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
    
    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        twobefore = 1
        onebefore = 2
        for i in range(2,n):
            twobefore, onebefore = onebefore, twobefore + onebefore
        return onebefore
    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for i in range(n):
            prev,current = current, prev+current
        return current  
                