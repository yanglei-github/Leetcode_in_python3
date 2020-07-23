# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:42:48 2020

@author: leiya
"""

'''
0702
注意判断末尾的特殊情况
二分法应用的时候特别要注意特殊情况，因为很有可能最后可能的答案根本就不再搜索的范围内，可能在list边界之外
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        if letters[right] <= target:
            return letters[0]
        while left < right:
            mid = (left+right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
    
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        #注意此处有等号
        if ord(target) >= ord(letters[right]):
            return letters[0]
        while left < right:
            mid = (left+right) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid
        return letters[left]
