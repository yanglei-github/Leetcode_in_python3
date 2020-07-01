# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:56:01 2020

@author: leiya
"""

#排列list中的某一项
#前一项的末尾元素如果大于后一项的开头元素，那么必定发生重叠
#在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。
#按区间的结尾进行排序
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x : x[1])
        i = 1
        count = 0
        while  1 <= i < len(intervals):
            if intervals[i-1][-1] > intervals[i][0]:
                count += 1
                intervals.remove(intervals[i])
            else:
                i += 1
        return count