# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:25:08 2019

@author: leiya
"""
#了解stack这个存储方式的优点
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        adic = {'{':'}','[':']','(':')'}
        for i in s:
            if i in adic:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i != adic[stack.pop()]:
                    return False
                else:
                    pass
        if len(stack) == 0:
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {'{':'}','[':']','(':')'}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                #']' in this case using len(stack) == 0 to avoid
                return False
        
        return len(stack) == 0
        #there must be no value in the stack means that perfectly match