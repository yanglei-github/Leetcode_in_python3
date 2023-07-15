# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:06:41 2020

@author: leiya
"""

#超时
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        res1 = []
        res2 = []
        
        for i in range(row):
            for j in range(col):
                visited = [[0 for _ in range(col)] for _ in range(row)]
                if visited[i][j] == 0:
                    
                    queue = [(i,j)]
                    if i == 0 or j == 0:
                        if [i,j] not in res1:
                            res1.append([i,j])
                    if i == row -1 or j == col - 1:
                        if [i,j] not in res2:
                            res2.append([i,j])
                    while queue:
                        cur_i,cur_j = queue.pop(0)
                        visited[cur_i][cur_j] = -1
                        
                        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                            temp_i = cur_i + x
                            temp_j = cur_j + y
                            
                            if 0 <= temp_i and temp_i < row and 0 <= temp_j and temp_j < col and visited[temp_i][temp_j] != -1 and matrix[temp_i][temp_j] <= matrix[cur_i][cur_j]:
                                if temp_i == 0 or temp_j == 0:
                                    if [i,j] not in res1:
                                        res1.append([i,j])
                                if temp_i == row -1 or temp_j == col - 1:
                                    if [i,j] not in res2:
                                        res2.append([i,j])
                                visited[temp_i][temp_j] = -1
                                queue.append((temp_i,temp_j))
        res = []
        for i in res1:
            if i in res2:
                res.append(i)
        return res