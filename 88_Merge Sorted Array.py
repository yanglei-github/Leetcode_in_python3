# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:29:08 2019

@author: leiya
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]
        compare = nums1[m-1]
     
        count = 0
        j = 0
        for i in range(n):
            while j >= 0 and j < m + count:
                if nums2[i] > nums1[j]:
                    j += 1
                else:
                    nums1.insert(j,nums2[i])
                    nums1.pop()
                    count += 1
                    break
            if nums2[i] > compare:
                nums1[m+count:m+count+len(nums2[i:])] = nums2[i:]
                break
            
            
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]
        compare = nums1[m-1]
        count = 0
        count1 = 0
        for i in range(len(nums2)):
            for j in range(count,m+count1):
                if nums2[i] > nums1[j]:
                    pass
                else:
                    nums1.insert(j,nums2[i])
                    nums1.pop() 
                    count = j
                    count1 += 1
                    break
            if nums2[i] > compare:
                nums1[count1+m:count1+m+len(nums2[i:])] = nums2[i:]
                break
            
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        if m == 0:
            nums1[:n] = nums2[:n]
            #nums1[:] = nums2[:]
      
        elif n != 0 and m != 0:
            for i in reversed(range(n)):
                for j in reversed(range(m)):
                    if nums2[i] >= nums1[j]:
                        nums1.insert(j+1,nums2[i])
                        nums1.pop()
                        count = 1
                        break
                
                if count == 0:
                    nums1.insert(0,nums2[i])
                    nums1.pop()
                count = 0


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m-1+n] = nums2[n-1]
                n -= 1
            else:
                nums1[m-1+n],nums1[m-1] = nums1[m-1],nums1[m-1+n]
                m -= 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]