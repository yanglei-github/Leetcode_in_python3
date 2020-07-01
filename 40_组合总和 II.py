# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:43:06 2020

@author: leiya
"""


''' 
i==start_index意味着如果是这一层第一次选元素是不存在重复的可能性的,这意味着如果在同一层中，
这次选的和上一次选的一样，那么必定是重复了，直接剪枝，否则会出现重复的解
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        def dfs(start_index,candidates,target,path,res):
            if target == 0:
                res.append(copy.deepcopy(path))
                return
            for i in range(start_index, len(candidates)):
                if candidates[i] <= target:
                    #i==start_index意味着如果是这一层第一次选元素是不存在重复的可能性的
                    if i > start_index and candidates[i] == candidates[i-1]:
                        continue
                        
                    path.append(candidates[i])
                    dfs(i+1,candidates,target-candidates[i],path,res)
                    path.pop()

        candidates.sort()
        res = []
        path = []
        start_index = 0
        dfs(start_index,candidates,target,path,res)
        return res
    
    
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res