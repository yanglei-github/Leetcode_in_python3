# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:02:56 2020

@author: leiya
"""
#每个dp存储以当前位置为结尾可以形成的最长上升子串
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #注意nums不存在的情况
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)
