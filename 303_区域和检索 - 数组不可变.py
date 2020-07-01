# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:36:58 2020

@author: leiya
"""

#注意class中变量要加self
#错位存储dp中的值
#i=1表示1之前的总和，而不是直接表示包括1的总和，这样会造成i=0时候出现问题
#dp[i],表示第i（index）个数（不含自己）之前的和
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0 for _ in range(len(nums)+1)]
        for i in range(1 , len(nums)+1):
            self.dp[i] = nums[i-1] + self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]
    
    
class NumArray:

    def __init__(self, nums: List[int]):
        #i=1表示1之前的总和，而不是直接表示包括1的总和，这样会造成i=0时候出现问题
        self.dp = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            self.dp[i] = self.dp[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]
