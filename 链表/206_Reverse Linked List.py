# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:34:05 2020

@author: leiya
"""

'''
0709
一开始不能直接将cur.next = pre因为之后还需要将cur移动到cur.next，如果一开始先动了cur.next，
那么下次cur移动到的cur.next的位置就不是一开始的位置了
'''
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