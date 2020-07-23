# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:59:40 2020

@author: leiya
"""

#有重复数字的情况
#相当于在判断的时候多了一种情况,nums[mid] == nums[right],这个时候只需要向前移动right一步，保证下次循环可以继续下去即可
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