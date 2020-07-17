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

'''
0715: cur and cur.next要同时判断，这道题与24可一起思考，即为什么要同时确保cur,cur.next都存在
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
    
    
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