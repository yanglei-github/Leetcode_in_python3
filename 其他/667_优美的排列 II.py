# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:18:59 2020

@author: leiya
"""

#构造法，技术型太强
#插排出现k个不同间隔的时候需要k+1个元素，剩下n-(k+1)个元素顺排，顺排只产生1个间隔，插排中出现的k个间隔中有一个是间隔1，
#与顺排的重复了，所以这样下来插排+顺排一共是K个，满足要求了
class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # 按顺序排好n-k个, 个数为1(邻差全是1)
        res = []
        for i in range(1, n-k):
            res.append(i)

        # 剩下k个插排, 个数为k-1(插排的邻差计算方法为k-1)
        count = -1
        for i in range(n-k, n+1):
            count += 1
            res.append(i)
            res.append(n-count)
            
        return res[0:n]