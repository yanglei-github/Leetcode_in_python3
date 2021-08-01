# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:59:58 2020

@author: leiya
"""

'''
0702
出现重复数字的情况是一定要先排序再剪枝，否则没有规律
'''
#回溯法的剪枝操作，需要首先对数组排序
#剪掉的是上一次刚被撤销，下一轮的搜索还会用到的数字
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False for _ in range(len(nums))]
        def dfs(visited,nums,path,res,depth):
            if depth == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if not visited[i]:
                    #如果visited[i-1] == True说明nums[i-1]正在被上一层选着呢，这个时候即使nums[i] == nums[i-1]
                    #但是如果其等于Flase说明他没有被上一层选择，同时已经在这一层被选择上且被弹出了或者是被这一层考虑选择过但是本层的筛选条件
                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True
                    path.append(nums[i])
                    dfs(visited,nums,path,res,depth+1)
                    visited[i] = False
                    path.pop()
        path = []
        res = []
        depth = 0
        nums.sort()
        dfs(visited,nums,path,res,depth)
        return res

#时间稍微优化
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        visited = [False for _ in range(size)]
        def dfs(visited,nums,size,path,res):
            if len(path) == size:
                res.append(path[:])
                return 
            for i in range(size):
                if not visited[i]:
                    if i >= 1 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    
                    visited[i] = True
                    path.append(nums[i])
                    dfs(visited,nums,size,path,res)
                    visited[i] = False
                    path.pop()
        path = []
        res = []
        nums.sort()
        dfs(visited,nums,size,path,res)
        return res
    
#无算法思想
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False for _ in range(len(nums))]
        def dfs(nums,path,res,depth,used):
            if depth == len(nums):
                if path not in res:
                    res.append(path[:])
                    return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums,path,res,depth+1,used)
                    used[i] = False
                    path.pop()
        dfs(nums,path,res,0,used)
        return res