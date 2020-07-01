# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:29:03 2019

@author: leiya
"""

'''
0626 updated:更新新的写法
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummynode = ListNode(0)
        pre = dummynode
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                pre = l2
                l2 = l2.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return dummynode.next
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy= ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        #must use this type because dummy and cur must be the same site at the beginning
        #use dummy save the head site of listnode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
        cur.next = l1 or l2
        
        return dummy.next
    
