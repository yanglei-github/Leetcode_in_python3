# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:34:05 2020

@author: leiya
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre