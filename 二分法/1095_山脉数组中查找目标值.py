# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:29:53 2020

@author: leiya
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        #mountaintop是山顶元素所在的index
        mountaintop = self.find_mountaintop(mountain_arr,0,size-1)
        res = self.find_from_sorted_arr(mountain_arr,0,mountaintop,target)
        if res != -1:
            return res
        return self.find_from_inversed_arr(mountain_arr,mountaintop+1,size-1,target)
    def find_mountaintop(self,mountain_arr,l,r):
        while l < r:
            mid = (l+r) // 2
            #上述情况每次取左中位数，一旦进入循环一定至少有两个元素
            #因此，左中位数一定有右边元素，数组下标不会越界
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                #相当于使用这个判断删除掉所有不符合要求的条件
                l = mid + 1
            else:
                #left和right互补
                r = mid
        return l
    def find_from_sorted_arr(self,mountain_arr,l,r,target):
        while l < r:
            mid = (l+r) // 2
            if mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        else:
            return -1
    
    def find_from_inversed_arr(self,mountain_arr,l,r,target):
        while l < r:
            mid = (l+r) // 2
            if mountain_arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        else:
            return -1
