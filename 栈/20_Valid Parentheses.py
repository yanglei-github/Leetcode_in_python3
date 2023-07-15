# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:25:08 2019

@author: leiya
"""

'''
0701:
    1.stack如果没有的情况需要特殊判断，比如说当前s[i]不再adict中但是stack中又没有东西，那么明显错了
    2.最后遍历完s后stack里有东西也不行，相当于没有匹配完全
0814:
    更细致的解体步骤
'''

class Solution:
    def isValid(self, s: str) -> bool:
        adict = {'(':')','[':']','{':'}'}
        stack = []
        for i in range(len(s)):
            if s[i] in adict.keys():
                stack.append(s[i])
            else:
                if stack and adict[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        
class Solution:
    def isValid(self, s: str) -> bool:
        #stack
        adict = {'(':')','{':'}','[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in adict:
                stack.append(s[i])
            else:
                if not stack or adict[stack.pop()] != s[i]:
                    return False
        if stack:
            return False
        return True


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