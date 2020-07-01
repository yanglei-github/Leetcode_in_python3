# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:46:32 2020

@author: leiya
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: 
                left[x] = i
            #right位置每次循环都更新
            right[x] = i
            #x如果在count中，就取出x作为key的value，若没有就取0
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count.keys():
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
