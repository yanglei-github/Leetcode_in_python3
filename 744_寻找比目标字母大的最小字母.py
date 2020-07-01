# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:42:48 2020

@author: leiya
"""


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
