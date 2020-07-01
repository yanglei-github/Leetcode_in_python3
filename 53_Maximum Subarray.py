# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:21:24 2019

@author: leiya
"""

#0623:updated
#V1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
#V1优化
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
       
#V1空间优化    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)): 
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
       

#----------------------------------------------------------------------

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        local_max,global_max =0,0
        for num in nums:
            local_max = max(0,local_max + num)
            global_max = max(global_max,local_max)
        return global_max
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = 0
        if max(nums) < 0:
            return max(nums)
        for i in range(len(nums)):
            local_max = max(nums[i]+local_max, 0)
            global_max = max(local_max, global_max)
        return global_max
            