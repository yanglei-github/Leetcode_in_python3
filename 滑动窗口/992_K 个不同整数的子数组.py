# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:37:46 2020

@author: leiya
"""

'''
0713
类比：560是一道前缀和的题，但是不能用这种滑动窗口的方法，问题出在题目的本质，
560要求找到和恰为k的连续子串个数，我们的方法只能用于恰为k个的情况，930特殊的点在于可以把和转化为求k个1，但是单纯求和恰为k滑动窗口是没办法解决的，
因为还是会出现start向前收缩的时候end需要往回收缩的情况，这一点我们的滑动窗口模板没办法解决

但是基于1 two sum问题，我们可以培养一种直觉，求和恰为k的这种模板是典型的前缀和解题思路，在一次遍历过程中先把当前看似无用的值存起来，
后面一旦发现有用再调用出来
'''
#与930解法类似，需要思考的是为什么需要这么去做
'''
904水果题相当于是这道题的基础，只是求了最多有两种类型的时候的情况，相当于求的atmost(A,2),因此没有借用前缀和的思想，
这道题之所以需要前缀和是因为它规定恰好为K个，因此可以用前缀和的思想来卡出恰好的种类数
与904的另一个区别是，输出不一样，904输出最多选择两种数字的情况下，最大的连续子序列长度，这道题是计算最多选择两种数字情况下有多少种子串的选择
'''
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        atmost的含义是最多（最多意味着可以小于等于，但不能超过）有K个不同种类的可能个数是多少个
        比如，当前有n个字符，判断成立，那么新多出来n个组合种类，可以从后向前看，n,(n,n-1),(n,n-1,n-2)...，一共新多出来n种方式
        之所以这么计算是因为可以用常规模式计算出这种定义形式的个数，无须虚拟的start进行试探
        因为这道题相对于leetcode.003等常规滑动窗口来说，收缩窗口的时候不是仅从start向前收缩就可以的，有些解可能需要start向前收缩的同时end向回收缩
        '''
        def atmost(A,k):
            start = 0
            adict = {}
            count = 0
            for end in range(len(A)):
                if A[end] not in adict:
                    adict[A[end]] = 1
                else:
                    adict[A[end]] += 1
                while len(adict) > k:
                    adict[A[start]] -= 1
                    if adict[A[start]] == 0:
                        del adict[A[start]]
                    start += 1
                #包含A[end]这个数在窗口[start,end]范围内所有可能的连续子串个数就等于当前窗口的长度
                count += end-start+1
            return count
        return atmost(A,K)-atmost(A,K-1)