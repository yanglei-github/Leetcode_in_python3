# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:52:29 2020

@author: leiya
"""

#前缀和+差分+哈希表
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #dict中存放到这个位置的奇数的个数
        adict = {}
        adict[0] = 1
        #temp是奇数的个数
        temp = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                temp += 1
            if temp - k in adict:
                res += adict[temp-k]
            if temp in adict:
                adict[temp] += 1
            else:
                adict[temp] = 1
                
        return res
    
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        res = 0
        adict = {}
        adict[0] = 1
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1
            if count - k in adict:
                res += adict[count-k]
            if count in adict:
                adict[count] += 1
            else:
                adict[count] = 1
        return res