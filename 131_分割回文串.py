# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:30:41 2020

@author: leiya
"""

#start_index用来表示每次找到子串的起始位置，for i in start_index表示以
#start_index开始找到结尾index i
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        def dfs(s,start_index,path,res):
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index,len(s)):
                if s[start_index:i+1] == s[start_index:i+1][::-1]:
                    path.append(s[start_index:i+1])
                    dfs(s,i+1,path,res)
                    path.pop()
                else:
                    continue
        
        res = []
        path = []
        start_index = 0
        dfs(s,start_index,path,res)
        return res

#超时
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        def dfs(s,start_index,path,res):
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index,len(s)):
                if not isPalindrome(s,start_index,i):
                    continue
                    
                else:
                    path.append(s[start_index:i+1])
                    dfs(s,i+1,path,res)
                    path.pop()

        def isPalindrome(s,left,right):
            while left < right:
                if s[left] != s[right]:
                    False
                else:
                    left += 1
                    right -= 1
            return True
        res = []
        path = []
        start_index = 0
        dfs(s,start_index,path,res)
        return res

#引入dp,用到的是leetcode.5最长回文串的dp思路
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        for j in range(1, length):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                    
        def dfs(s,start_index,path,res):
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index,len(s)):
                if not dp[start_index][i]:
                    continue
                    
                else:
                    path.append(s[start_index:i+1])
                    dfs(s,i+1,path,res)
                    path.pop()

        
        res = []
        path = []
        start_index = 0
        dfs(s,start_index,path,res)
        return res
    
