# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:33:00 2020

@author: leiya
"""

'''
0714
间隔K比较好想，问题在于不要找当前node的前一个node，因为这样需要for _ in range(k+1)，理论上没问题
但是当倒数第k个恰好是头节点的时候，fur就变成了none.next，需出现错误
'''

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur = head
        fur = head
        for _ in range(k):
            fur = fur.next
        while fur:
            cur = cur.next
            fur = fur.next
        return cur
    
    
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        
        #two pointers 相距K
        pre = head
        cur = head
        for _ in range(k):
            cur = cur.next
        while cur:
            pre = pre.next
            cur = cur.next
        return pre