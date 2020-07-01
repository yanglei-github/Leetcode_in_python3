# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:29:04 2020

@author: leiya
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone= {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        def dfs(start_index,digits,path,res):
            if start_index == len(digits):
                res.append(path[:])
                return

            
            for j in range(len(phone[digits[start_index]])):
                path += phone[digits[start_index]][j]
                dfs(start_index+1,digits,path,res)
                path = path[:-1]
        path = ''
        res = []
        start_index = 0
        dfs(start_index,digits,path,res)
        return res
