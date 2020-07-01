# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:36:38 2020

@author: leiya
"""


'''
0701:相当于基于stack的add binary
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = None
        carry = 0
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 or stack2 or carry:
            if stack1:
                temp1 = stack1.pop()
            else:
                temp1 = 0
            if stack2:
                temp2 = stack2.pop()
            else:
                temp2 = 0
            cur_val = temp1 + temp2 + carry
            cur_use = cur_val % 10
            carry = cur_val // 10
            cur_node = ListNode(cur_use)
            cur_node.next = pre
            pre = cur_node
        return pre
    
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
    
