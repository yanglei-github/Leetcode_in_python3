# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:15:34 2020

@author: leiya
"""



'''
0711
On时间复杂度实现，间隔n一次扫描
'''

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        fur = cur
        pre = None
        for _ in range(n):
            fur = fur.next
        #注意判断将头节点去掉的特殊情况
        if not fur:
            return head.next
        while fur:
            pre = cur
            cur = cur.next
            fur = fur.next
        pre.next = cur.next
        return head
    
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
            