# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:36:10 2020

@author: leiya
"""


#[] is not None,空列表不是None
#辅助栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helpstack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.helpstack) == 0 or x < self.helpstack[-1]:
            self.helpstack.append(x)
        else:
            self.helpstack.append(self.helpstack[-1])

    def pop(self) -> None:
        if len(self.stack) != 0:       
            self.stack.pop()
            self.helpstack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.helpstack) != 0:
            return self.helpstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()