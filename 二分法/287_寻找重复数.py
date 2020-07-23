# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:32:12 2020

@author: leiya
"""

#典型根据抽屉原理，无须情况下也可使用
#注意只有一个重复的整数
'''
我的经验是把定义区间成为左闭右闭区间，左右边界是无差别的，弄成左闭右开，反而增加了思考的复杂程度；
明确 int = left + ( right - left ) / 2 这里除以 2 是下取整；
明确 while(left <= right) 和 while(left < right) 这两种写法其实在思路上有本质差别， while(left <= right) 在循环体内部直接查找元素，
而 while(left < right) 在循环体内部一直在排除元素，第 2 种思路在解决复杂问题的时候，可以使得问题变得简单；
始终在思考下一轮搜索区间是什么，把它作为注释写到代码里面，就能帮助我们搞清楚边界是不是能取到，等于、+1 、-1 之类的细节；
思考清楚每一行代码背后的语义是什么，保证语义上清晰，也是写对代码，减少 bug 的一个非常有效的策略。
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = (right + left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里

            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left