# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:59:40 2020

@author: leiya
"""

#没有相同数字存在
#有想象力的二分法，二分法本质就在于如何信誓旦旦的排除掉那些不符合要求的元素(divide the search space into two and see which direction to go.
#只不过这个过程是一半一半的找，
#即通过改变left,right，不断的二分，重要点在于基于何种条件移动他们
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

