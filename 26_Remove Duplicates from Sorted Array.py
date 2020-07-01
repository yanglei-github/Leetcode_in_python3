# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:13:11 2019

@author: leiya
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1 
        return len(nums)
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1 
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        count = 1
        j = 0
        for i in range(1,n):
            if nums[i-j] != nums[i-j-1]:
                count += 1
            else:
                nums.pop(i-j-1)
                j += 1
        return count

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = 0
        #if we let count = 1,when len(nums)=1,nums[count] must be out of range
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count+1