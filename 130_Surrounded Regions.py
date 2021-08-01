# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:20:21 2020

@author: leiya
"""


"""
updated 0725
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        def bfs(board,x,y):
            if board[x][y] == 'O':
                board[x][y] = 'temp'
                queue = [(x,y)]
                while queue:
                    tempx,tempy = queue.pop(0)
                    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                        curx = tempx + i
                        cury = tempy + j
                        if 0<=curx<row and 0<=cury<col and board[curx][cury]=='O':
                            board[curx][cury] = 'temp'
                            queue.append((curx,cury))
        
        for j in [0,col-1]:
            for i in range(row):
                bfs(board,i,j)
        for i in [0,row-1]:
            for j in range(col):
                bfs(board,i,j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'temp':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board
    
'''
0710 updated
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #首先将四周的O全部找到（区别于橘子，一个一个找，
        #因为前一个找到的可能会影响下一次的选择，不需要重复再找了，可以节省找的效率），之后bfs找到跟他们相邻的O,全都置为B
        #对一层一层的找不敏感，即每一层找完以后不需要做什么特殊的操作，因此可以把一个点的所有层找完再去找下一个点
        row = len(board)
        if not board:
            return
        col = len(board[0])
        def bfs(i,j):
            if board[i][j] == 'O':
                board[i][j] = 'B'
                queue = []
                queue.append((i,j))
                while queue:
                    tempx,tempy = queue.pop(0)
                    for x,y in [(1,0),(-1,0),(0,-1),(0,1)]:
                        curx = x + tempx
                        cury = y + tempy
                        if 0<=curx<row and 0<=cury<col and board[curx][cury] == 'O':
                            board[curx][cury] = 'B'
                            queue.append((curx,cury))
        for j in [0,col-1]:
            for i in range(row):
                bfs(i,j)
        for i in [0,row-1]:
            for j in range(col):
                bfs(i,j)
               
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #首先将四周的O全部找到（区别于橘子，一个一个找，
        #因为前一个找到的可能会影响下一次的选择，不需要重复再找了，可以节省找的效率），之后bfs找到跟他们相邻的O,全都置为B
        #对一层一层的找不敏感，即每一层找完以后不需要做什么特殊的操作，因此可以把一个点的所有层找完再去找下一个点
        row = len(board)
        if not board:
            return
        col = len(board[0])
        def dfs(i,j):
            if board[i][j] == 'O':
                board[i][j] = 'B'
                stack = [(i,j)]
                while stack:
                    tempx,tempy = stack.pop()
                    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                        curx = tempx + x 
                        cury = tempy + y
                        if 0<=curx<row and 0<=cury<col and board[curx][cury] == 'O':
                            board[curx][cury] = 'B'
                            stack.append((curx,cury))

        for j in [0,col-1]:
            for i in range(row):
                dfs(i,j)
        for i in [0,row-1]:
            for j in range(col):
                dfs(i,j)
               
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                    
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #首先将四周的O全部找到（区别于橘子，一个一个找，
        #因为前一个找到的可能会影响下一次的选择，不需要重复再找了，可以节省找的效率），之后bfs找到跟他们相邻的O,全都置为B
        #对一层一层的找不敏感，即每一层找完以后不需要做什么特殊的操作，因此可以把一个点的所有层找完再去找下一个点
        row = len(board)
        if not board:
            return
        col = len(board[0])
        def dfs(i,j):
            if board[i][j] == 'O':
                board[i][j] = 'B'
                for x,y in [(1,0),(0,-1),(0,1),(-1,0)]:
                    curx = x + i
                    cury = y + j
                    if 0<=curx<row and 0<=cury<col and board[curx][cury] == 'O':
                        dfs(curx,cury)
        for j in [0,col-1]:
            for i in range(row):
                dfs(i,j)
        for i in [0,row-1]:
            for j in range(col):
                dfs(i,j)
               
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                    


#previous version                  
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

