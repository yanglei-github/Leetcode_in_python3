# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:32:18 2020

@author: leiya
"""


'''
0712:规范化滑动窗口模板
0718:进一步规范化模板；另外这道题实际上是992的基础版本，建议做完后直接跳转至992
     此外这道题也不存在状态回缩的问题，关于状态回缩，可参考3，209的分析思路
'''

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        max_len = float('-inf')
        adict = {}
        for end in range(len(tree)):
            if tree[end] in adict:
                adict[tree[end]] += 1
            else:
                adict[tree[end]] = 1
            while len(adict) > 2:
                adict[tree[start]] -= 1
                if adict[tree[start]] == 0:
                    del adict[tree[start]]
                start += 1
            max_len = max(max_len,end-start+1)
        if max_len == float('-inf'):
            return 0
        else:
            return max_len
        
        
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        adict = {}
        max_len = float('-inf')
        for end in range(len(tree)):
            if tree[end] not in adict:
                adict[tree[end]] = 1
            else:
                adict[tree[end]] += 1
            while len(adict.keys()) > 2:
                adict[tree[start]] -= 1
                if adict[tree[start]] == 0:
                    del adict[tree[start]]
                start += 1
            max_len = max(max_len,end-start+1)
        return max_len
    
    
    
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        #只含有两个不同字符的所有连续子串中最长的连续子串的长度
        start = 0
        adict = {}
        max_len = 0
        for end in range(len(tree)):
            if tree[end] not in adict:
                adict[tree[end]] = 1
            else:
                adict[tree[end]] += 1
            while len(adict.keys()) > 2:
                adict[tree[start]] -= 1
                if adict[tree[start]] == 0:
                    del adict[tree[start]]
                start += 1
            max_len = max(max_len,end-start+1)
        return max_len