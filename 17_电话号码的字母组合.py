# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:29:04 2020

@author: leiya
"""

'''
0705
总结：
回溯问题最关键的一点在于明白每一层的解空间是什么，每深入一层，各个层次间的解空间如何变化，这种变化是需要随着递归函数不断传入的，
以此来告诉代码每一层的找解的条件是什么，在什么空间里找，这道题不需要marked,visited这种空间来标记用过的解，因为每一层他的解空间完全不同，
因此上一层的解空间跟下一层互斥不相容，不需要visited来避免找到上一层访问过的解
0710
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        adict= {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        def dfs(start_index,adict,path,res):
            if start_index == len(digits):
                res.append(path[:])
                return

            for num in adict[digits[start_index]]:
                path += num
                dfs(start_index+1,adict,path,res)
                path = path[:-1]
        res = []
        path = ''
        start_index = 0
        dfs(start_index,adict,path,res)
        return res
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        #注意hashtable中的key最好是字符串类型
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
                #这里对字符串进行删除时，不能用path - phone[digits[start_index]][j],因为字符串不支持-操作，只能切片
                path = path[:-1]
        path = ''
        res = []
        start_index = 0
        dfs(start_index,digits,path,res)
        return res
