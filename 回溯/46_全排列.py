# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:51:10 2020

@author: leiya
"""


'''
220326
for循环控制每一层，dfs在通过for循环选定该层数据后进入下一层
0716:如果希望在调用dfs之后用到res，就不能在dfs这个函数里对res重新赋值，只能对res进行append之类的操作，一旦重新赋值
res就不是原来传入的res了,如果只是对现有res做一些操作，那么还是原来的res
'''
#不能用start_index来减小子空间，只能用used来判断子空间取值
class Solution:
    def permute(self, nums):
        #设置现场
        #递归
        #恢复现场
        used = [False for _ in range(len(nums))]
        res = []
        #print(id(res))
        path = []
        def put(nums,depth,used,path,res):
            if depth == len(nums):
                #此处需要深拷贝
                res.append(copy.deepcopy(path))
                #print(id(res))
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
        #print(id(res))
        return res
solution = Solution()
solution.permute([1,2,3])

