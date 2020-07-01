# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:28:11 2020

@author: leiya
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next