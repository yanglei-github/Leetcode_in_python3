# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:59:40 2020

@author: leiya
"""

#有重复数字的情况
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right = right - 1
            else:
                right = mid

        return nums[left]