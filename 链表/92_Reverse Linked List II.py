# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:12:32 2020

@author: leiya
"""

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        fixm = dummyNode

        for i in range(m - 1):
            fixm = fixm.next
        
        # reverse the [m, n] nodes
        pre = None
        cur = fixm.next
        for i in range(n - m + 1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        fixm.next.next = cur
        fixm.next = pre

        return dummyNode.next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummynode = ListNode(0)
        dummynode.next = head
        fixm = dummynode
        for i in range(m-1):
            fixm = fixm.next
        pre = None
        cur = fixm.next
        for i in range(n-m+1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        fixm.next.next = cur
        fixm.next = pre
        return dummynode.next