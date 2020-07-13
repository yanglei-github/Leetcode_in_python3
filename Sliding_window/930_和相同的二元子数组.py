# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:19:38 2020

@author: leiya
"""

'''
参考992，1248
给定一个0，1数组，你可以选择最多S个1和任意个0，你的选择数减去 给定一个0，1数组，你可以选择最多S - 1个1和任意个0，你的选择数
'''
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMostK(A, S):
            #因为用到了atmostK(A,S-1),S要是输入的是0，S-1就是负值了，会出现问题
            if S < 0:
                return 0
            start = 0
            count = 0
            sum_ = 0
            for end in range(len(A)):
                sum_ += A[end]
                while sum_ > S:
                    sum_ -= A[start]
                    start += 1
                count += end - start + 1
            return count
        return atMostK(A, S) - atMostK(A, S - 1)
    
    
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMostK(A, S):
            if S < 0:
                return 0
            i = res = 0

            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res
        return atMostK(A, S) - atMostK(A, S - 1)