# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:54:22 2020

@author: leiya
"""

#注意相同元素的处理
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = (left+right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
                #去掉right还有 mid指向和原来right相同的值，所以本质上去掉right无关紧要
            elif numbers[mid] == numbers[right]:
                right -= 1
            else:
                right = mid
        return numbers[left]