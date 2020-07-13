# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:52:40 2020

@author: leiya
"""

#前缀和+哈希表优化(存储前缀和各个值出现的个数)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        adict = {}
        adict[0] = 1
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            '''
            下面的两个if是有先后顺序的，必须严格按照当前顺序，因为必须先更新res再更新adict[cur_sum]
            '''
            if cur_sum - k in adict:
                res += adict[cur_sum-k]
            if cur_sum in adict:
                adict[cur_sum] += 1
            else:
                adict[cur_sum] = 1
        return res
    
#滑动窗口，超时
def subarraySum(nums, k):
    start = 0
    count = 0
    res = 0
    while start < len(nums):
        for i in range(start, len(nums)):
            res += nums[i]
            if res == k:
                count += 1
                
            
        res = 0
        start += 1
    return count

a = subarraySum([1,2,1,2,1],3)
print(a)


    
    
    
    
    
    