# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:42:19 2020

@author: leiya
"""
#0625 updated:queue = []也可以在双重循环外面初始化，因为每次循环以后queue又变成空的了
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        
        max_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue = []
                    count = 1
                    grid[i][j] = 0
                    queue.append((i,j))
                    while queue:
                        tempx,tempy = queue.pop(0)
                        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                            curx = tempx + x
                            cury = tempy + y
                            if 0 <= curx < row and 0 <= cury < col and grid[curx][cury] == 1:
                                grid[curx][cury] = 0
                                count += 1
                                queue.append((curx,cury))
                    max_count = max(max_count,count)
        return max_count
#BFS
#无须一层一层分着计数
#需要一个一个找root，而不是一次把全部root压进queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total_res = 0
        for i in range(row):
            for j in range(col):
                res = 0
                if grid[i][j] == 1:
                    queue = []
                    res += 1
                    grid[i][j] = 0
                    queue.append((i,j))
                    while queue:
                        cur_i, cur_j = queue.pop(0)
                        for x, y in [(0,1),(0,-1),(-1,0),(1,0)]:
                            temp_i = cur_i + x
                            temp_j = cur_j + y
                            if 0 <= temp_i and temp_i < row and 0 <= temp_j and temp_j < col and grid[temp_i][temp_j] == 1:
                                grid[temp_i][temp_j] = 0
                                res += 1
                                queue.append((temp_i,temp_j))
                total_res = max(res,total_res)
        return total_res

#dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid,i,j):
            if 0 <= i and i < row and 0 <= j and j < col and grid[i][j] == 1:
                #每次要标记访问过的节点
                grid[i][j] = 0
                return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
            else:
                return 0
        row = len(grid)
        col = len(grid[0])
        result = 0
        for i in range(row):
            for j in range(col):
                result = max(result, dfs(grid,i,j))
        return result 
                        