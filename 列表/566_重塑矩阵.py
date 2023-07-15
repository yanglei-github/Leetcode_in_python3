# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:14:22 2020

@author: leiya
"""

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        new_num = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(row*col):
            new_num[i//c][i%c] = nums[i//col][i%col]
            
        return new_num