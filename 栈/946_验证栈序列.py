# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:48:56 2020

@author: leiya
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        start = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[start]:
                stack.pop()
                start += 1
        if not stack:
            return True
        else:
            return False