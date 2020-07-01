# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:54:01 2020

@author: leiya
"""

#已知无重复元素，所以不需要去重
#类比于全排列问题
#不包含重复数组一般都需要排序来解决重复问题
#这道题无须使用深度，因为每次return的情况不是由depth决定，而是由target决定，
#也可以将target理解成depth，其作为一个return的衡量指标决定dfs的递归何时退出


'''
0625 updated:start_index的重要性，第一次第一层找到一个数之后，在第二次选取第一层数后，后面的递归应该都从这个数后的所有数中寻找解集
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        def dfs(start,candidates,target,path,res):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(i,candidates,target-candidates[i],path,res)
                    path.pop()
        res = []
        path = []
        start = 0
        dfs(start,candidates,target,path,res)
        return res
    
    
#2020/06/13 未优化版
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #不包含重复数组一般都需要排序来解决重复问题
        if not candidates:
            return []
        candidates.sort()
        def dfs(candidates,target,path,res):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(len(candidates)):
                path.append(candidates[i])
                dfs(candidates[i:],target-candidates[i],path,res)
                path.pop()
        res = []
        path = []
        dfs(candidates,target,path,res)
        return res
    
#2020/06/13 优化版
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #不包含重复数组一般都需要排序来解决重复问题
        if not candidates:
            return []
        candidates.sort()
        def dfs(candidates,target,path,res):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(len(candidates)):
                if candidates[i] <= target:  
                    path.append(candidates[i])
                    dfs(candidates[i:],target-candidates[i],path,res)
                    path.pop()
                else:
                    break
        res = []
        path = []
        dfs(candidates,target,path,res)
        return res   

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []
        def dfs(candidates,target,path):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(candidates[i:],target-candidates[i],path)
                path.pop()
        path = []
        dfs(candidates,target,path)
        return res
    

#非模板型回溯法
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []
        def dfs(candidates,target,path):
            if target == 0:
                res.append(path)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                #特别注意此处不能用path.append(candidates[i]),因为这个东西没有返回值，只是对path进行了操作
                #在下一次dfs中相当于传入了Nonetype，从而产生错误
                dfs(candidates[i:],target-candidates[i],path + [candidates[i]])
        path = []
        dfs(candidates,target,path)
        return res