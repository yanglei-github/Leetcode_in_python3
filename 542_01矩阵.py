# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:54:03 2020

@author: leiya
"""


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        res_mark = [[-1 for _ in range(col)] for _ in range(row)]
        queue = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    res_mark[i][j] = 0
                    queue.append((i,j))
        depth = 0
        while queue:
            depth += 1
            current_len = len(queue)
            for _ in range(current_len):
                cur_i, cur_j = queue.pop(0)
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    temp_i = cur_i + x
                    temp_j = cur_j + y
                    if 0 <= temp_i and temp_i < row and 0 <= temp_j and temp_j < col and res_mark[temp_i][temp_j] == -1:
                        res_mark[temp_i][temp_j] = depth
                        queue.append((temp_i,temp_j))
        return res_mark