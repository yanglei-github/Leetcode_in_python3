# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:02:39 2020

@author: leiya
"""
#浅拷贝与深拷贝，特殊情况的处理
#即在这种情况下只有一个元素的时候会出现问题，因为一开始对nums进行了切片操作
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums)+1)]
        dp1 = dp[:]
        dp[2:] = nums[1:]
        dp1[2:] = nums[:-1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2]+dp[i], dp[i-1])
            dp1[i] = max(dp1[i-2]+dp1[i], dp1[i-1])
        return max(dp[-1], dp1[-1])
    
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre2 = 0
        pre1 = 0
        for i in range(1, len(nums)):
            cur = max(pre1, pre2 + nums[i])
            pre2 = pre1
            pre1 = cur
        pre4 = 0
        pre3 = 0
        for i in range(0, len(nums)-1):
            cur1 = max(pre3, pre4 + nums[i])
            pre4 = pre3
            pre3 = cur1
        return max(pre1, pre3)