# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:29:51 2020

@author: leiya
"""

'''
0714
'''
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummynode = ListNode(100)
        dummynode.next = head
        pre = dummynode
        cur = head
        while cur.val != val:
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return dummynode.next
    
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummynode = ListNode(0)
        dummynode.next = head
        pre = dummynode
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                #注意返回位置，找到了就返回，否则放到while外面永远结束不了，构成了死循环
                return dummynode.next
            else:
                pre = cur
                cur = cur.next