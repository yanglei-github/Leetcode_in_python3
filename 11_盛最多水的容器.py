# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:54:07 2020

@author: leiya
"""

#双指针，考虑状态的剪枝
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0
        while start < end:
            if height[start] < height[end]:
                res = max(res, height[start] * (end - start))
                start += 1
            else:
                res = max(res, height[end] * (end - start))
                end -= 1
        return res