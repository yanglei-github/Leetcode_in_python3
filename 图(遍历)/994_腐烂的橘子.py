# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:14:29 2020

@author: leiya
"""

'''
0710
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count_one = 0
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    count_one += 1
        if count_one == 0:
            return 0
        if not queue:
            return -1
        
        #按层遍历
        time = -1
        while queue:
            current_len = len(queue)
            for _ in range(current_len):
                x,y = queue.pop(0)
                for tempx,tempy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    curx = tempx+x
                    cury = tempy+y
                    if 0<=curx<row and 0<=cury<col and grid[curx][cury] == 1:
                        grid[curx][cury] = 2
                        queue.append((curx,cury))
            time += 1

        for eachrow in grid:
            if 1 in eachrow:
                return -1
        return time
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
        flag = 0
        #如果一开始就没有新鲜的橘子那么直接返回0
        for each_row in grid:
            if 1 in each_row:
                flag = 1
        if flag == 0:
            return 0
        count = -1
        while queue:
            current_len = len(queue)
            for _ in range(current_len):
                tempx,tempy = queue.pop(0)
                for x,y in [(1,0),(-1,0),(0,-1),(0,1)]:
                    curx = x + tempx
                    cury = y + tempy
                    if 0 <= curx < row and 0 <= cury < col and grid[curx][cury] == 1:
                        grid[curx][cury] = 2
                        queue.append((curx,cury))
            count += 1
        for each_row in grid:
            if 1 in each_row:
                return -1
        return count
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        row = len(grid)
        col = len(grid[0])
        #判断特殊情况,即是否一开始grid中就没有新鲜橘子
        count = 0
        for eachrow in grid:
            if 1 not in eachrow:
                count += 1
            else:
                break
        if count == row:
            return 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
        #找到最后一个的时候实际上也压入了队列中，相当于多进行了一次循环，计数时需要减去
        step = -1
        while queue:
            current_len = len(queue)
            for _ in range(current_len):
                i,j = queue.pop(0)
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    temp_i = i + x
                    temp_j = j + y
                    if 0 <= temp_i and temp_i < row and 0 <= temp_j and temp_j < col and grid[temp_i][temp_j] == 1:
                        grid[temp_i][temp_j] = 2
                        queue.append((temp_i,temp_j))
            step += 1
        for eachrow in grid:
            if 1 in eachrow:
                return -1
        
        return step


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cur_queue = []
        row = len(grid)
        col = len(grid[0])
        if row == 1 and col == 1 and grid[0][0] != 1:
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    cur_queue.append((i,j))
        step = -1
        
        while cur_queue:
            next_queue = []
            for i, j in cur_queue:
                
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    temp_i = i + x
                    temp_j = j + y
                    if 0 <= temp_i and temp_i < row and 0 <= temp_j and temp_j < col and grid[temp_i][temp_j] == 1:
                        grid[temp_i][temp_j] = 2
                        next_queue.append((temp_i,temp_j))
            cur_queue = next_queue
            step += 1
        for eachrow in grid:
            if 1 in eachrow:
                return -1
        
        return step