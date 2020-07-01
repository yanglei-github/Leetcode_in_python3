# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:32:28 2020

@author: leiya
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.queue:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()