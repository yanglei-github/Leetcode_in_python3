# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:04:54 2020

@author: leiya
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:        
        maxans = 0
        dp = [0]*len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                # 避免python负数的从后往前取值
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0 ) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) +2
                maxans = max(maxans, dp[i])
        return maxans