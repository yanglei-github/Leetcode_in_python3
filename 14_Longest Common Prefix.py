# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:50:09 2019

@author: leiya
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if strs == []:
            return ''
        #找到输入列表中最短的字符串的索引值，用这个最短的索引值的字符串作为搜索字符串
        newstrs = list(map(len,strs))
        min_index = newstrs.index(min(newstrs))
        for i in range(len(strs[min_index])):
            for j in strs:
                
                if strs[min_index][i] != j[i]:
                    return res
            res = res + strs[min_index][i]
        return res
    
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if strs == []:
            return ''
        #找到输入列表中最短的字符串的索引值，用这个最短的索引值的字符串作为搜索字符串
        newstrs = list(map(len,strs))
        min_index = newstrs.index(min(newstrs))
        for i in range(len(strs[min_index])):
            for j in strs:
                if j == min_index:
                    pass
                else:
                    if strs[min_index][i] != j[i]:
                        return res
            res = res + strs[min_index][i]
        return res
        
    
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        strs.sort(key=lambda x:len(x))
        if strs[0] == '':
            return ''
        result = ""
        for i in range(len(strs[0])):
            sets = set(string[i] for string in strs)
            if len(sets) == 1:
                result += sets.pop()
            else:
                return result
        return result

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result
    