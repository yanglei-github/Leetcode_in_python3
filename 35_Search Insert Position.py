# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:07:04 2019

@author: leiya
"""

#0620 updated:重新更新二分法模板，注意left = mid时需要向上取整即mid = (left+right+1) // 2,为了避免死循环出现
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #注意结尾的边界值问题
        #需要判断特例，因为这种情况left,right都遍历不到
        if nums[right] < target:
            return right + 1
        #注意此处没有等于号
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #需要判断特例，因为这种情况left,right都遍历不到
        if nums[right] < target:
            return right+1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left
#----------------------------------------------------------------------------
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
                else:
                    pass
            return len(nums)
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if target > nums[i]:
                count += 1
            
        return count
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        if target in nums:
            #more faster
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    count += 1
            return count
        