# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:42:39 2020

@author: leiya
"""

#136异或问题的变体，区别在于这道题已经排好序，并且要求在logn内解决
#实际上通过仅对偶数索引进行二分，我们实现了log(n/2) = logn
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if mid % 2 == 1:
                #为何此处mid - 1不会越界，因为mid此时为奇数，也就意味着前面一定有一个偶数index,永远不会越界
                mid -= 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]