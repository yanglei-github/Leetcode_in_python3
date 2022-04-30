# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:52:40 2020

@author: leiya
"""

'''
0725
为什么这题不可以用双指针/滑动窗口：因为nums[i]可以小于0，也就是说右指针i向后移1位不能保证区间会增大，
左指针j向后移1位也不能保证区间和会减小。给定j，i的位置没有二段性，vice versa。
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        adict = {}
        adict[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in adict:
                count += adict[cur_sum-k]
            if cur_sum not in adict:
                adict[cur_sum] = 1
            else:
                adict[cur_sum] += 1
        return count
    
    
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


    
    
    
    
    
    