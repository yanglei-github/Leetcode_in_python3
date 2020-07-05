# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:32:18 2020

@author: leiya
"""


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