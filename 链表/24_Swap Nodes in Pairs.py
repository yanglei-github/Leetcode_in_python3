# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:49:03 2020

@author: leiya
"""

#date:0516
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummynode = ListNode(0)
        dummynode.next = head
        pre = dummynode
        cur = head
        
        '''
        fur = cur.next
        while cur and fur:
        这种写法是不对的，我们只更新cur，通过更新cur来间接更新fur，如果直接这么写会十分费力，在循环里会引入判断，即判断更新后的cur是否存在
        因为一旦cur不存在,fur = cur.next就会报错
        '''
        while cur and cur.next:
            fur = cur.next
            pre.next = fur
            pre = cur
            #cur.next = fur.next 这步非常关键，因为如果后面有单一节点，那么没这步就连不上了
            cur.next = fur.next
            cur = fur.next
            fur.next = pre
        return dummynode.next
    
    
#构建虚假表头+单指针
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummynode = ListNode(0)
        pre = dummynode
        pre.next = head
        while pre.next is not None and pre.next.next is not None:
            l1 = pre.next
            l2 = pre.next.next
            l1.next = l2.next
            l2.next = l1
            pre.next = l2
            pre = l1
        return dummynode.next
            
