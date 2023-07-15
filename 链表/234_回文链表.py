# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:38:15 2020

@author: leiya
"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #转换成array再判断：可能有负值存在
        if not head:
            return True
        cur = head
        s = []
        while cur:
            s.append(cur.val)
            cur = cur.next
        if s == s[::-1]:
            return True
        else:
            return False