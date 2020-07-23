# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:34:21 2020

@author: leiya
"""

'''
0723
我们对于二分法应该有一定的直觉性，这个直觉就在于现有的已知nums是否是排好序的，因为二分法只能应用于排好序的前提下
'''
'''
0702
1. 左右逼近思路,这个思路之所以必要，是因为这道题相对于35题存在重复数字，一旦有两个重复数字88,我们必须明确该选重复数字中的左还是右
选左就是右边逼近，因为舍弃了右边的重复数字, right = mid-1,选右就是左边逼近，因为舍弃了左边的重复数字，left = mid + 1
可以假设现在只有两个重复数字构成的list，如果要舍弃右边的数，一开始必须取右中位数，然后让left=mid，即可

2. nums如果为空的特殊情况需要提前判断

3.二分查找不但要提前判断找的index是否在搜索范围内,还要判断最后在搜索范围内找到的唯一index对应的value是否符合要求

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #明显遍历两次
        res = [-1,-1]
        if not nums:
            return res
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return res
        else:
            res[0] = left
        right = len(nums) - 1
        while left < right:
            mid = (left+right+1) // 2
            #nums[mid] == target的时候需要移动left而不是移动right，可以假设只有两个相同元素的nums
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = left
        return res
    
#只要有left-mid,就用left+right+1 // 2来解决out of range的问题
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        if not nums:
            return res
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            #找到起始位置，所以找到等于情况时直接移动right至该位置，至于该位置之后是否有相同数不重要，找起始位置从右边逼近
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return res
        else:
            res[0] =left
        right = len(nums) - 1 
        while left < right:
            #取右中位数
            mid = (left+right+1) // 2
            if nums[mid] > target:
                right = mid - 1
            #找终止位置，如果此时找到等于情况不能直接移动right，因为会排除该位置后出现相同元素的可能，这是应该移动left至该位置，找终止位置从左边逼近
            else:
                left = mid
        res[1] = left 
        return res