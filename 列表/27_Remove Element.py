# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:16:20 2019

@author: leiya
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i <= len(nums)-1:
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointers from start and end
        if not nums:
            return 0
        pre = 0
        post = len(nums) - 1
        while pre < post:
            if nums[pre] == val:
                if nums[post] == val:
                    post -= 1
                else:
                    nums[pre],nums[post] = nums[post],nums[pre]
                    pre += 1
            else:
                pre += 1
        if nums[pre] == val:
            return pre
        else:
            return pre + 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pre = 0
        post = len(nums) - 1
        while pre <= post:
            if nums[pre] == val:
                nums[pre],nums[post] = nums[post],nums[pre]
                post -= 1
            else:
                pre += 1
        return post + 1
        