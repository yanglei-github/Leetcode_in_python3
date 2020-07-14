# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 07:38:08 2020

@author: leiya
"""

'''
0714
用辅助栈颠倒链表
'''
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        res = []
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while stack:
            pop_node = stack.pop()
            res.append(pop_node)
        return res
    
    
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]