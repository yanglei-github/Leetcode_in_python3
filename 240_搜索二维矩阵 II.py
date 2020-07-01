# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:19:28 2020

@author: leiya
"""

#从左下角开始查找
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col <= len(matrix[0])-1:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False

#从右上角开始查找，不过此时需要判断matrix是否存在，因为一开始要使用matrix[0]，不存在的话会报错
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while col >= 0 and row <= len(matrix) - 1:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False