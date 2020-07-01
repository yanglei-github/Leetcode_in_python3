# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:54:59 2020

@author: leiya
"""
#双dp问题
#用两个up, down dp数列
#小循环内也要用max实时更新当前值 up[i] = max(up[i], down[j] + 1)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #注意空的情况
        if not nums:
            return 0
        down = [1 for _ in range(len(nums))]
        up = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                    #这里不能用else,注意相等元素出现的可能性
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        
        return max(max(down),max(up))