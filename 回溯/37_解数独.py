# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:38:28 2020

@author: leiya
"""

'''
0717
0718:注意str与int的转换
     区别于一般回溯法的难点在于我们需要通过递归这种方式每次移动当前方格的位置，这道题不单单需要
     考虑解空间的变化，还需要去考虑不停的移动位置，跟给所有位置找到合适的解空间，一旦回溯法和图相结合，dfs,bfs就不再仅仅充当线性深入
     下一层的probe,而是更加多变的指向下一层的不同选择
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col = [set() for i in range(9)]
        row = [set() for i in range(9)]
        sqr = [[set() for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    col[j].add(board[i][j])
                    row[i].add(board[i][j])
                    sqr[i//3][j//3].add(board[i][j])
        
        def dfs(i, j):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    self.flag = True
                    return
                if j < 8:
                    dfs(i, j+1)
                else:
                    dfs(i+1, 0)
            else:
                for ch in range(1, 10):
                    ch = str(ch)
                    if ch not in col[j] and ch not in row[i] and ch not in sqr[i//3][j//3]:
                        #print(i, j, ch)
                        col[j].add(ch)
                        row[i].add(ch)
                        sqr[i//3][j//3].add(ch)
                        board[i][j] = ch
                        if i == 8 and j == 8:
                            self.flag = True
                            return
                        if j < 8:
                            dfs(i, j+1)
                        else:
                            dfs(i+1, 0)
                        if self.flag: 
                            return
                        board[i][j] = '.'
                        col[j].remove(ch)
                        row[i].remove(ch)
                        sqr[i//3][j//3].remove(ch)
        self.flag = False
        dfs(0, 0)
        
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