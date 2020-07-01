# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:18:21 2020

@author: leiya
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left+right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left