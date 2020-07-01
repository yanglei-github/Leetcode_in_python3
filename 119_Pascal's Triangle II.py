# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:35:46 2020

@author: leiya
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])
        return res[rowIndex]

