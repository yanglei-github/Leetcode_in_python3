# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:52:29 2020

@author: leiya
"""


'''
0712
前缀和+滑动窗口
参考：930,992(based on 904)
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(nums,k):
            start = 0
            count = 0
            odd_count = 0
            for end in range(len(nums)):
                if nums[end] % 2 != 0:
                    odd_count += 1
                while odd_count > k:
                    if nums[start] % 2 != 0:
                        odd_count -= 1
                    start += 1
                count += end-start+1
            #注意return返回的位置，要在for循环外返回
            return count
        return atmost(nums,k) - atmost(nums,k-1)
    
    
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