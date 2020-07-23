# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:54:31 2019

@author: leiya
"""



#69,35题都是我们可以确定解一定在left,right可以遍历到的位置，所以左后while left == right弹出后无须进一步判断left,right最后指向的同一个位置是否是题解
#换句话说，一定有解，那么排除了所有不可能的解，最后的解一定是left或者right指向的解，无须进一步判断
#0620 updated:切换二分法模板
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2 + 1
        while left < right:
            mid = (left+right+1) // 2
            #注意这里有等号
            if mid ** 2 <= x:
                left = mid
            else:
                right = mid - 1
        #该模板的好处在于最后无须思考返回left还是right，应为两者一样,但是有时候需要判断一下left,right是否是需要的解，因为在while里没有判断
        return left
    
    
#双指针切换
#一个数的平方根小于等于这个数的一半,
#right = x//2 + 1是为了照顾到1这个特例
#最后要找的结果是其平方小于等于x的最大的mid
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        right = x // 2 + 1
        left = 0
        #不加等于号1,9这些例子不能通过
        while left <= right:
            mid = (right+left)//2
            if mid ** 2 <= x:
                res = mid
                left = mid + 1
                
            else:
                right = mid - 1
        return res

class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while x / n > n:
            n += 1
        if x/n == n:
            return n
        else:
            return n-1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (right+left) // 2
            if mid > x/mid:
                right = mid - 1
            else:
                left = mid + 1
        return right