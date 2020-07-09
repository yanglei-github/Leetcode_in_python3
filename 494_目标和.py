# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:26:04 2020

@author: leiya
"""

'''
找到nums一个正子集和一个负子集，使得总和等于target，统计这种可能性的总数

sum(P) - sum(N) = target （两边同时加上sum(P)+sum(N)）
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N) (因为 sum(P) + sum(N) = sum(nums))
2 * sum(P) = target + sum(nums)
sum(P) = (target + sum(nums)) // 2
'''
#可以转换成求子集和的问题，即01背包问题
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: 
            return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            j = P
            while j >= num:
                dp[j] = dp[j] + dp[j - num]  #dp[j]为不选当前i，dp[j-num]为选择当前i对应的value
                j -= 1
        return dp[-1]