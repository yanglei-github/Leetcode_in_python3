# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:22:48 2020

@author: leiya
"""

'''
0901 updated
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_num(mat, val):
            row = 0
            col = len(mat) - 1
            cnt = 0
            while row < len(mat) and col >= 0:
                if mat[row][col] <= val:
                    cnt += col + 1
                    row += 1
                else:
                    col -= 1
            return cnt
        
        left = matrix[0][0]
        right = matrix[-1][-1]
        '''
        left == right时返回，保证最后找到的值一定存在于matrix中
        '''
        while left < right:
            mid = (left+right) // 2
            cnt = count_num(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left
    
    
#此题在240的基础上采用二分查找
#此时的二分查找实际上指定的left,right都是实际数值，而不是index，这一点要区分一下
#这种方式加上240的方法实际上相当于将matrix按从小到大的顺序展平，count_num实现的操作相当于这个目的，只不过实际上没有这么做
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # 计算小于等于目标值的元素个数，根据递增规则，从右上角开始查找
        def count_num(m, target):
            i = 0
            j = len(m) - 1
            ans = 0
            while i < len(m) and j >= 0:
                if m[i][j] <= target:
                    ans += j + 1
                    i += 1
                else:
                    j -= 1
            return ans
        #思路：左上角元素最小，右下角元素最大，计算小于等于中间值的元素个数
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left+right) // 2
            count = count_num(matrix,mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
        
    
    
#method 2
        left = matrix[0][0]
        right = matrix[-1][-1]
        # 二分法查找，注意等号的存在
        while left <= right:
            mid = (left + right) // 2
            count = count_num(matrix, mid)
            
            if count < k:
                
                left = mid + 1
            else:
                #两者相同时候，其实还是将r减小了1位，所以最后应该输出left，
                #此时不直接输出mid是因为mid表示的数值不一定在matrix中存在
                right = mid - 1
        #非常存，无论何时都要输出left
        return left
    
    