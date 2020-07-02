# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:17:12 2020

@author: leiya
"""
'''
二分用于在较短数组中查询到分割位置
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        
        left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
        mid1 = (left + right) // 2
        mid2 = half_len - mid1
        
        while left < right:
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = half_len - mid1
        
        if mid1 == 0: 
            max_of_left = nums2[mid2-1]
        elif mid2 == 0: 
            max_of_left = nums1[mid1-1]
        else: 
            max_of_left = max(nums1[mid1-1], nums2[mid2-1])

        if (len1 + len2) % 2 == 1:
            return max_of_left

        if mid1 == len1: 
            min_of_right = nums2[mid2]
        elif mid2 == len2: 
            min_of_right = nums1[mid1]
        else: 
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2

