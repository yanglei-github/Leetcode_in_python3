# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:23:16 2020

@author: leiya
"""

#定长滑动窗口
#based on 28
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        ori_dict = collections.Counter(s1)
        
        start = 0
        end = len(s1) - 1
        for i in range(end, len(s2)):
            if collections.Counter(s2[start:i+1]) == ori_dict:
                return True
            start += 1
            
        return False