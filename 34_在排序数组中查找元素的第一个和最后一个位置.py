# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:34:21 2020

@author: leiya
"""

#只要有left-mid,就用left+right+1 // 2来解决out of range的问题
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        if not nums:
            return res
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            #找到起始位置，所以找到等于情况时直接移动right至该位置，至于该位置之后是否有相同数不重要，找起始位置从右边逼近
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return res
        else:
            res[0] =left
        right = len(nums) - 1 
        while left < right:
            #取右中位数
            mid = (left+right+1) // 2
            if nums[mid] > target:
                right = mid - 1
            #找终止位置，如果此时找到等于情况不能直接移动right，因为会排除该位置后出现相同元素的可能，这是应该移动left至该位置，找终止位置从左边逼近
            else:
                left = mid
        res[1] = left 
        return res