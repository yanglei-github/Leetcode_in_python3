# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:34:35 2020

@author: leiya
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        nums1Len = len(nums1)
        nums2Len = len(nums2)
        p1, p2 = 0, 0
        res = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        while p1 < nums1Len and p2 < nums2Len:
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return res