# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:29:08 2019

@author: leiya
"""



'''
0702:从后向前比，即同时比两者最末尾的数，谁大谁放到nums1末尾0的位置上
思路是每次把所有大于nums2[n]的nums1中的所有值交换到后面，loop跳出后放以此n，可以概括成放尽可能多次的m,之后放一次n，然后移动nums2中的指针n
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_size = len(nums1) - 1
        n = n-1
        m = m-1
        while n >= 0:
            while m >= 0 and nums1[m] > nums2[n]:
                nums1[m],nums1[total_size] = nums1[total_size], nums1[m]
                total_size -= 1
                m -= 1
            nums1[total_size] = nums2[n]
            n -= 1
            total_size -= 1
            
            
            
            
'''
0705
这道题的难点在于m不存在的情况下如何处理还没有放入nums1中的nums2的值
建议用0702版代码，默认考虑了特殊情况的处理，不需要单独处理
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #思路，从后面开始比，然后放
        size = len(nums1) - 1
        n = n-1
        m = m-1
    
        while n >= 0:
            if m < 0:
                nums1[:size+1] = nums2[:n+1]
                break
            if nums1[m] < nums2[n]:
                nums1[size] = nums2[n]
                n -= 1
            else:
                nums1[size], nums1[m] = nums1[m], nums1[size]
                m -= 1
            size -= 1
            
            
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