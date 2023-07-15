# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:41:43 2020

@author: leiya
"""


'''首先找到从左块开始最小块的大小。如果前 k 个元素为 [0, 1, ..., k-1]，
可以直接把他们分为一个块。当我们需要检查 [0, 1, ..., n-1] 中前 k+1 个元素是不是 [0, 1, ..., k] 的时候，
只需要检查其中最大的数是不是 k 就可以了。
'''

class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: 
                ans += 1
        return ans