# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:49:03 2020

@author: leiya
"""

#date:0516
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummynode = ListNode(0)
        dummynode.next = head
        pre = dummynode
        cur = head
        while cur and cur.next:
            fur = cur.next
            pre.next = fur
            pre = cur
            cur.next = fur.next
            cur = fur.next
            fur.next = pre
        return dummynode.next
    
    
#构建虚假表头+单指针
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummynode = ListNode(0)
        pre = dummynode
        pre.next = head
        while pre.next is not None and pre.next.next is not None:
            l1 = pre.next
            l2 = pre.next.next
            l1.next = l2.next
            l2.next = l1
            pre.next = l2
            pre = l1
        return dummynode.next
            
