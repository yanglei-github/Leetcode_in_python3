# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:38:08 2020

@author: leiya
"""

#引入dummynode,然后将tail首先指向dummynode，然后移动tail判断即将翻转的链表个数是否足够
class Solution:
    def reverse_linked(self, head, tail):
        pre = None
        cur = head
        #注意，此处与单纯翻转链表不同，因为我们相当于在一个长链表中翻转某一部分的链表，
        #因此不能用while cur:来作为终止条件，因为这会找到长链表的最后一个元素
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return tail, head
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        hair = pre
        tail = pre
        while head:
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return hair.next
                else:
                    nex = tail.next
            head, tail = self.reverse_linked(head, tail)
            
            pre.next = head
            tail.next = nex
            head = nex
            pre = tail
        return hair.next