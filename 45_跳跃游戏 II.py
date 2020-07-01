# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:11:38 2020

@author: leiya
"""

#每次找到可以跳到的最远位置，把指针指向最远位置，继续遍历list，
#当前遍历到的值如果在上一个最远位置内且可以跳到更远的位置，那么说明第二次可以从这里开始跳（这也就意味着第一次已经跳完了）,可以到达更远的位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        maxbound, end, step = 0, 0, 0
        for i in range(len(nums)-1):
            maxbound = max(maxbound, i + nums[i])
            if i == end:#已经在上一次可能做的落脚点中找到这步的最远落脚点，可以跳了
                step += 1
                end = maxbound#更新最大落脚点
        return step