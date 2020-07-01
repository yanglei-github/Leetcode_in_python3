# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:34:16 2019

@author: leiya
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            forward = cur.next
            while forward:
                if cur.val == forward.val:
                    forward = forward.next
                else:
                    break
            cur.next = forward
            cur = cur.next
        return head