# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:48:30 2020

@author: leiya
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            #之所以加这个判断是因为当前位置如果是0但是同时fast也是0，那么我们需要按住不动，一直移动fast去找fast指向不为0的数
            #如果之后找到的数都是0，那么就意味着找完了，因此fast < len(nums)作为最后的while判断条件
            if nums[slow] != 0:
                slow += 1
            fast += 1
    