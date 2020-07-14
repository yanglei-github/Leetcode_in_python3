# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:11:54 2020

@author: leiya
"""

#使用双指针，一个指针每次移动一个节点，一个指针每次移动两个节点，如果存在环，那么这两个指针一定会相遇。

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #快慢指针
        #注意一开始head不存在的情况
        if not head:
            return False
        
        '''
        一开始尽量让快慢指针错开，因为一开始指向相同的node的话，在只有一个node且无环的情况下会误判
        '''
        slow = head
        fast = head.next
        while fast and fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next
        if slow == fast:
            return True
        else:
            return False
        
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow is not None and fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

#运行时间过长
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while slow is not None:
            while fast is not None:
                if slow == fast.next:
                    return True
                else:
                    fast = fast.next
            slow = slow.next
            fast = slow
        return False