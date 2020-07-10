# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:51:10 2020

@author: leiya
"""

#不能用start_index来减小子空间，只能用used来判断子空间取值
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #设置现场
        #递归
        #恢复现场
        used = [False for _ in range(len(nums))]
        res = []
        path = []
        def put(nums,depth,used,path,res):
            if depth == len(nums):
                #此处需要深拷贝
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if not used[i]:
                    #设置现场需要两步
                    path.append(nums[i])
                    used[i] = True
                    #递归
                    put(nums,depth+1,used,path,res)
                    #恢复现场需要两步
                    used[i] = False
                    path.pop()
        put(nums,0,used,path,res)
        return res

