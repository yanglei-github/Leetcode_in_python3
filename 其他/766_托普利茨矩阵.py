# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:56:50 2020

@author: leiya
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i+1 < row and j + 1 < col:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
        return True