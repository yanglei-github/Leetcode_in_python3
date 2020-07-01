# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:38:54 2020

@author: leiya
"""

'''
只要哈希表中的值出现次数为偶数，就可以成为最长回文串的一部分；
如果是奇数，次数减一也可以成为最长回文串的一部分；
第一次出现的奇数可以不用减一，放在最长回文串的中间。
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        adict = {}
        count = 0
        flag = 0
        for i in range(len(s)):
            if s[i] not in adict:
                adict[s[i]] = 1
            else:
                adict[s[i]] += 1
        for word in adict.keys():
            if adict[word] % 2 == 0:
                count += adict[word]
            else:
                #之所以这么搞是因为完全有可能没有奇数个的元素存在
                count += adict[word] - 1
                flag = 1
        return count + flag