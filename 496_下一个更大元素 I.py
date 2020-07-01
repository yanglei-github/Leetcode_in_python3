# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:37:52 2020

@author: leiya
"""

#503变体
#遍历nums2,因为实际上答案的顺序是存在于nums2中的，将nums2中每次遍历到的值在nums1中找到对应的index压入栈中，之后跟739一样
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums2)):
            while stack and nums1[stack[-1]] < nums2[i]:
                res[stack.pop()] = nums2[i]
            if nums2[i] in nums1:
                stack.append(nums1.index(nums2[i]))
        return res