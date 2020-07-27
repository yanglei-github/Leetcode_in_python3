# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:17:33 2020

@author: leiya
"""

'''
0718
'''
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        max_len = float('-inf')
        count_one = 0
        for end in range(len(A)):
            if A[end] == 1:
                count_one += 1
            while count_one + K < end-start+1:
                if A[start] == 1:
                    count_one -= 1
                start += 1
            max_len = max(max_len,end-start+1)
        if max_len == float('-inf'):
            return 0
        else:
            return max_len
        
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        #标准滑动窗口
        start = 0
        max_len = float('-inf')
        count = 0
        for end in range(len(A)):
            if A[end] == 1:
                count += 1
            #while start < len(A) and end-start+1 > count + K:
            while end-start+1 > count + K:
                if A[start] == 1:
                    count -= 1
                start += 1
            max_len = max(max_len,end-start+1)
        return max_len