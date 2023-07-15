# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:02:58 2020

@author: leiya
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.' * n for _ in range(n)]
        def put_queen(row,n,res):
            if row == n:
                path = []
                for i in range(n):
                    path.append(copy.deepcopy(board)[i])
                res.append(path)
                return
            for j in range(n):
                if can_place(row,j):
                    board[row] = '.'*j + 'Q' + '.'*(n-j-1)
                    put_queen(row+1,n,res)
                    board[row] = '.' * n 
            
        def can_place(x,y):
            for i in range(x):
                if board[i][y] == 'Q':
                    return False
            for j in range(y):
                if board[x][j] == 'Q':
                    return False

            for i in range(x):
                if x+y-i <= n-1:
                    if board[i][x+y-i] == 'Q':
                        return False
            
            for i in range(x):
                if n-1 >= i-(x-y) >= 0:
                    if board[i][i-(x-y)] == 'Q':
                        return False
            return True
        res = []
        put_queen(0,n,res)
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        cols = [0] * n
        #eg.n=8, [1->7,0,-1->-7]共15个即2n-1
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output