# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:52:49 2020

@author: leiya
"""

#谁指向谁，第一个谁在等式左边
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ahead = headA
        bhead = headB
        while ahead != bhead:
            if ahead is None:
                ahead = headB
            else:
                ahead = ahead.next
            if bhead is None:
                bhead = headA
            else:
                bhead = bhead.next
        return ahead