# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:20:21 2020

@author: leiya
"""

#DFS，在边界上找到一个O之后迅速找它相邻的有没有O,用dfs找。
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(i,j):
            board[i][j] = 'B'
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                temp_x = i + x
                temp_y = j + y
                if 1 <= temp_x < row and 1 <= temp_y < col and board[temp_x][temp_y] == 'O':
                    dfs(temp_x,temp_y)
    
      
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[row-1][j] == 'O':
                dfs(row-1,j)
        
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][col-1] == 'O':
                dfs(i,col-1)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
        return board
    
 
#BFS  
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

