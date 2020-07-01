# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:28:53 2020

@author: leiya
"""

#关键在于埃拉托斯特尼筛法，简称埃式筛，也叫厄拉多塞筛法：
#要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。
#res = [1,1,1]
#res[0:2] = [0,0]
#print(res)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0 
        res = [1] * n
        res[0:2] = [0,0]
        for i in range(2, int(n**0.5)+1):
            if res[i] == 1:
                j = i * i
                while j < n:
                    res[j] = 0
                    j = j + i
        return res.count(1)