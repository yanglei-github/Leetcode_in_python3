# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:20:42 2020

@author: leiya
"""

'''
类比树，每次拿出树的一层，然后一个一个拿出这层中的所有node，判断每个node的下一个node是否可以
正好probe下探到结束点，同时将符合通道要求但是没有触及到结束点的该层的下一层node放到下一层统一的list中
如果这层所有的node全部找完了，但是所有的node的下一层node没有到结束点，那么我们进行下一层遍历。
总体上来说，每轮循环遍历树的一层node，因为这层node是上一层可以走到的node，走到这一层node需要的距离一样，这样
一层一层的找，知道找到一层中的某个node的bfs中的下一层node恰好是结束点，这个时候就可以结束了

Note:值得注意的就是，该层符合通道要求的下一层node找到后应该置为-1，这样该层中其他node找到这个node的时候就不用在记录了，
同时也保证了下一层node的bfs循环的时候找到该节点时不会记录，因为该节点明显可以在上一层抵达，在这层再去抵达没有意义，因为一定会造成路径的浪费
'''

#0625 updated:
#注意这是方形网格，row=col，注意特殊情况的处理
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if row == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = [(0,0)]
        count = 1
        while queue:
            current_len = len(queue)
            for i in range(current_len):
                tempx,tempy = queue.pop(0)
                for x,y in [(0,1),(0,-1),(1,-1),(1,0),(1,1),(-1,0),(-1,-1),(-1,1)]:
                    curx = tempx + x
                    cury = tempy + y
                    if 0 <= curx < row and 0 <= cury < col and grid[curx][cury] == 0:
                        if curx == row - 1 and cury == col - 1:
                            return count + 1
                        grid[curx][cury] = 1
                        queue.append((curx,cury))
            count += 1
        return -1 
    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        grid[0][0] = -1
        res = 1
        cur_queue = [(0,0)]
        while cur_queue:
            next_queue = []
            for i,j in cur_queue:
                for x, y in [(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1)]:
                    temp_i = i + x
                    temp_j = j + y
                    if temp_i == n-1 and temp_j == n-1:
                        return res + 1
                    if not 0 <= temp_i < n or not 0 <= temp_j < n:
                        continue
                    if grid[temp_i][temp_j] == 1:
                        continue
                    if grid[temp_i][temp_j] == -1:
                        continue
                    if grid[temp_i][temp_j] == 0:
                        grid[temp_i][temp_j] = -1
                        next_queue.append((temp_i,temp_j))
            cur_queue = next_queue
            res += 1
        return -1

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        grid[0][0] = 1
        res = 1
        cur_queue = [(0,0)]
        while cur_queue:
            next_queue = []
            for i,j in cur_queue:
                for x, y in [(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1)]:
                    temp_i = i + x
                    temp_j = j + y
                    if temp_i == n-1 and temp_j == n-1:
                        return res + 1
                    if not 0 <= temp_i < n or not 0 <= temp_j < n:
                        continue
                    if grid[temp_i][temp_j] == 1:
                        continue
                    
                    if grid[temp_i][temp_j] == 0:
                        grid[temp_i][temp_j] = 1
                        next_queue.append((temp_i,temp_j))
            cur_queue = next_queue
            res += 1
        return -1

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        grid[0][0] = 1
        res = 1
        queue = [(0,0)]
        while queue:
            current_len = len(queue)
            for i in range(current_len):
                a,b = queue.pop(0)
                for x, y in [(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1)]:
                    temp_i = a + x
                    temp_j = b + y
                
                    if temp_i == n-1 and temp_j == n-1:
                        return res + 1
                    if not 0 <= temp_i < n or not 0 <= temp_j < n:
                        continue
                    if grid[temp_i][temp_j] == 1:
                        continue
                    
                    if grid[temp_i][temp_j] == 0:
                        grid[temp_i][temp_j] = 1
                        queue.append((temp_i,temp_j))
            
            res += 1
        return -1


