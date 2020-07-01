# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:19:06 2020

@author: leiya
"""


#0623:updated
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: 
            return 0
        res = 1
        if n < 0: 
            x, n = 1 / x, -n
        while n:
            if n & 1: 
                res *= x
            #x *= x放到后面更新
            x *= x
            n >>= 1
        return res
    
    
#快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mulpow(n):
            if n == 0:
                return 1.0
            
            y = mulpow(n // 2)
            if n % 2 == 0:
                return y*y
            else:
                return y*y*x
        if n >=0 :
            return mulpow(n)
        else:
            return 1.0/mulpow(-n)
        

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

