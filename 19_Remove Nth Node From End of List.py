# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:15:34 2020

@author: leiya
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        n_inorder = count - n + 1
        pre = None
        cur = head
        count1 = 1
        while cur is not None:
            if count1 == n_inorder:
                if pre is None:
                    head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                count1 += 1
                pre = cur
                cur = cur.next
        return head
            