# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:39:11 2020

@author: leiya
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res >= 2 ** 31 else res

'''
如果不这么做的话测试用例是[-2,-2,1,1,-3,1,-3,-3,-4,-2] 的时候，就会输出 4294967292。 
其原因在于Python是动态类型语言，在这种情况下其会将符号位置的1看成了值，而不是当作符号“负数”。 
这是不对的。 正确答案应该是 - 4，-4的二进制码是 1111...100，就变成 2^32-4=4294967292，解决办法就是 减去 2 ** 32 。

'''