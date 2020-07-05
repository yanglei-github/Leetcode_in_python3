# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:35:16 2020

@author: leiya
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 0:
            return False
        sum_num = sum(nums)
        #如果数组和为奇数，那么一定找不到解
        if sum_num % 2 == 1:
            return False
        target = sum_num // 2
        #一开始需要给列多加一位，我们需要考虑背包容量是0的情况
        dp = [[False for _ in range(target+1)] for _ in range(size)]
        if nums[0] < target:
            #i == 0，表示第一个物品，只不过这里index从0开始
            dp[0][nums[0]] = True
        
        for i in range(1, size):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    #在[0,i]这个区间选择某些数是他们的和恰好等于j,这个时候针对区间尾nums[i]可以选择选或者不选
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]

#优化时间复杂度
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 0:
            return False
        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False
        target = sum_num // 2
        dp = [[False for _ in range(target+1)] for _ in range(size)]
        #dp[0][0] = True
        for i in range(size):
            dp[i][0] = True
        if nums[0] < target:
            dp[0][nums[0]] = True
        
        for i in range(1, size):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            if dp[i][target]:
                return True
        return dp[-1][-1]

#状态压缩
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 0:
            return False
        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False
        target = sum_num // 2
        dp = [False for _ in range(target+1)]
        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True
        for i in range(1, size):
            j = target
            #注意此时j要倒叙开始
            while j >= nums[i]:
                if dp[target]:
                    return True
                dp[j] = dp[j] or dp[j-nums[i]]
                j -= 1
        return dp[-1]

