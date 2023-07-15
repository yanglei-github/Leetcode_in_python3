# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:17:18 2020

@author: leiya
"""
#特殊排序方法: pairs.sort(key=lambda x:x[1])

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1 for _ in range(len(pairs))]
        pairs.sort(key=lambda x:x[1])
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)