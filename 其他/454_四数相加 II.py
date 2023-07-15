# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:19:10 2020

@author: leiya
"""

#两个两个的找，降低时间复杂度
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        length = len(A)
        res = 0
        adict = {}
        for x in range(length):
            for y in range(length):
                
                if A[x]+B[y] not in adict:
                    adict[A[x]+B[y]] = 1
                else:
                    adict[A[x]+B[y]] += 1
        for i in range(length):
            for j in range(length):
                if -(C[i] + D[j]) in adict:
                    res += adict[-(C[i] + D[j])]
        return res
    
#先找三个再找最后一个 N3复杂度
 class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        length = len(A)
        res = 0
        adict = {}
        for x in range(length):
            for y in range(length):
                for z in range(length):
                    if A[x]+B[y]+C[z] not in adict:
                        adict[A[x]+B[y]+C[z]] = 1
                    else:
                        adict[A[x]+B[y]+C[z]] += 1
        for i in range(length):
            if -D[i] in adict:
                res += adict[-D[i]]
        
        return res       
    