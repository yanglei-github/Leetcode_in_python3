# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:36:38 2020

@author: leiya
"""

#双栈问题
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummynode = ListNode(0)
        
        stack1, stack2 = [], []
        carry = 0
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 or stack2 or carry:
            if stack1:
                val1 = stack1.pop()
            else:
                val1 = 0
            if stack2:
                val2 = stack2.pop()
            else:
                val2 = 0
            value = val1 + val2 + carry
            valnode = value % 10
            carry = value // 10
            node = ListNode(valnode)
            node.next = dummynode.next
            dummynode.next = node
                
        return dummynode.next