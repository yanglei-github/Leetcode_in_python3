# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:22:38 2020

@author: leiya
"""

#0625: updated
#dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        stack = []
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    stack.append((i,j))
                    grid[i][j] = '0'
                    while stack:
                        tempx,tempy = stack.pop()
                        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                            curx = tempx + x
                            cury = tempy + y
                            if 0 <= curx < row and 0 <= cury < col and grid[curx][cury] == '1':
                                grid[curx][cury] = '0'
                                stack.append((curx,cury))
                    count += 1
        return count
#bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        queue = []
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    #找到某个符合条件的node后立刻标记
                    grid[i][j] == '0'
                    queue.append((i,j))
                    while queue:
                        cur_i, cur_j = queue.pop(0)
                        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                            temp_i = cur_i + x
                            temp_j = cur_j + y
                            if 0 <= temp_i < row and 0 <= temp_j < col and grid[temp_i][temp_j] == '1':
                                grid[temp_i][temp_j] = '0'
                                queue.append((temp_i,temp_j))
                    count += 1
        return count
    

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid,i,j):
            if 0<=i and i < row and 0<=j and j<col and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(grid,i+1,j)
                dfs(grid,i-1,j) 
                dfs(grid,i,j-1) 
                dfs(grid,i,j+1)
                
        if not grid:
            return 0 
        row = len(grid)
        col = len(grid[0])
        result = 0
        for i in range(row):
            for j in range(col):
                #此处必须加判断，因为只有为1的时候才进行计数，要是不需要计数完全可以不用加判断
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    result += 1
        return result
    
    
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        #用len(grid)和len(grid[0])可以消除特殊情况的判断
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

