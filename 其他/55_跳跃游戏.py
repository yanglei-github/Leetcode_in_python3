# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:53:17 2020

@author: leiya
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        res = 0
        end = 0
        for i in range(len(nums)-1):
            res = max(res, i+nums[i])
            if res >= len(nums)-1:
                return True
            
            if i == end:
                if i == res:
                    return False
                else:
                    end = res


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

