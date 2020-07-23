# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:42:39 2020

@author: leiya
"""


'''
0723:这道题其实比较特殊，不符合一般的二分法模板，我们尽可能不要对mid+1，mid-1进行这类操作，可以类比153题，可以避免的时候尽量避免，因为可能会Out of range
'''
#136异或问题的变体，区别在于这道题已经排好序，并且要求在logn内解决
#为什么找偶数索引，因为正常来说一对一对构成的nums，偶数索引应该和后面的奇数索引构成一对，一旦他俩不等，说明结果肯定在该偶数index之前（包括该偶数）
#实际上通过仅对偶数索引进行二分，我们实现了log(n/2) = logn
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if mid % 2 == 1:
                #为何此处mid - 1不会越界，因为mid此时为奇数，也就意味着前面一定有一个偶数index,永远不会越界
                mid -= 1
            #此处mid+1不会越界是因为每次取mid是取左中位数，永远有右边的数，当没有右边数的时候left==right，该退出了，不会再执行这一步
            #对于只有一个数的数组，left一开始就等于right，因此不会进while,进而不会执行到这一步
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]