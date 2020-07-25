# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:49:26 2020

@author: leiya
"""

#注意边界值
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums)+2)]
        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        #if not nums:
            #return 0
        dp = [0 for i in range(len(nums)+2)]
        dp[2:] = nums
        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-2]+dp[i], dp[i-1])
        return dp[-1]
    
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        pre2 = 0
        pre1 = 0
        for i in range(len(nums)):
            cur = max(pre2+nums[i], pre1)
            pre2 = pre1
            pre1 = cur      
        return pre1