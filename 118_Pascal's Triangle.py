# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:42:56 2020

@author: leiya
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1], [1,1]]
        
        for i in range(3,numRows+1):
            cur_res = [1]
            for j in range(1,len(res[i - 2])):
                cur_res.append(res[i-2][j-1]+ res[i-2][j])
            cur_res.append(1)
            res.append(cur_res)
        return res
    
    
    
    
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])               
        return res
                