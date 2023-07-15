# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:29:17 2019

@author: leiya
"""
#2020/2/6
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
                

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        adict = {}
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp not in adict:
                adict[numbers[i]] = i
            else:
                return [adict[temp]+1,i+1]       


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''two pointers because of sorted list'''
        start = 0
        end = len(numbers) - 1
        while end > start:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start+1,end+1]