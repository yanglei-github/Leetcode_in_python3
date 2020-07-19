# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:54:26 2020

@author: leiya
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[i//3][j//3]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        square[i//3][j//3].add(board[i][j])
        return True