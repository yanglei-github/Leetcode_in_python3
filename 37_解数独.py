# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:38:28 2020

@author: leiya
"""


class Solution:
    def solveSudoku(self, board) -> None:
        # 对 board[i][j] 进行穷举尝试
        def backtrack(board, i, j):
            m, n = 9, 9
            if j == n:   # 走到9才越界，进入下一行
                return backtrack(board, i+1, 0)
            if i == m:   # 走到最后一行，找到一个可行解
                return True
            if board[i][j] != '.':   # 当前是预设数字，直接跳到下一个
                return backtrack(board, i, j+1)

            ch_list = ['1','2','3','4','5','6','7','8','9']
            for ch in ch_list:
                if not isValid(board, i, j, ch):   # 如果遇到不合法的数字，则跳过
                    continue

                board[i][j] = ch   # 做选择
                if backtrack(board, i, j+1):  # 如果找到一个可行解，立即结束
                    return True
                board[i][j] = '.'   # 撤销选择
            # 穷举完 1~9，依然没有找到可行解，此路不通
            return False

        # 判断 board[i][j] 是否可以填入 n
        def isValid(board, r, c, n):
            for i in range(9):
                # 判断行是否存在重复
                if board[r][i] == n: return False
                # 判断列是否存在重复
                if board[i][c] == n: return False
                # 判断 3 * 3 方框是否存在重复
                if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == n:
                    return False
            return True

        backtrack(board, 0, 0)