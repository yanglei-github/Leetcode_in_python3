# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:58:37 2020

@author: leiya
"""

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0 for _ in range(len(A))]
        count = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                count += dp[i]
        return count