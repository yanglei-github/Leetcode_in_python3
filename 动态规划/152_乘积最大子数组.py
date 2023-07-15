# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:01:49 2020

@author: leiya
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = nums[:]
        min_dp = nums[:]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i], max_dp[i-1]*max_dp[i], max_dp[i]*min_dp[i-1])
            min_dp[i] = min(min_dp[i], min_dp[i-1]*min_dp[i], min_dp[i]*max_dp[i-1])
        return max(max(max_dp),max(min_dp))