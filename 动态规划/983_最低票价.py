# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:25:58 2020

@author: leiya
"""
#用max(0, day-7)防止越界问题

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_pointer = 0
        dp = [0 for _ in range(0, days[-1]+1)]
        
        for day in range(1, len(dp)):
            if day != days[day_pointer]:
                dp[day] = dp[day-1]
            else:
                #用max(0, day-7)防止越界问题
                dp[day] = min(dp[max(0, day - 7)]+costs[1],
                                dp[max(0, day - 30)]+costs[2],
                                dp[max(0, day -1 )]+costs[0])
                day_pointer += 1
        return dp[-1]