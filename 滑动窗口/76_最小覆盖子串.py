# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:51:05 2020

@author: leiya
"""



'''
0713
对输出的更新要放在while内，题目要性质决定，因此最后要加min_len == float('inf')判断是否有特殊情况
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        min_len = float('inf')
        res = '' 
        target = {}
        counter = {}
        for i in t:
            if i not in target:
                target[i] = 1
            else:
                target[i] += 1
            #这里省了很大力气，因为counter和target现在key个数一样，我们比较的时候只需要比较counter中key的value是否严格小于target即可
            counter[i] = 0
        
        def contains(counter, target):
            for k in counter:
                '''
                千万注意这里是<，不能改成!=，因为counter[k] > target[k]是允许的，
                counter[k]只要不比target[k]小就ok,小说明元素包含不全
                '''
                if counter[k] < target[k]:
                    return False
            return True

        for end in range(len(s)):
            if s[end] in counter:
                counter[s[end]] += 1
            #while start < len(s) and contains(counter, target):
            while contains(counter, target):
                if end - start + 1 < min_len:
                    min_len = end-start+1
                    res = s[start:end + 1]
                if s[start] in target:
                    counter[s[start]] -= 1
                start += 1

        if min_len == float('inf'):
            return ""  
        else:
            return res
        
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        min_len = float('inf')
        res = ''
        n = len(s)
        #用两个字典去比较窗口是否满足条件
        target = {}
        counter = {}
        for i in t:
            if i not in target:
                target[i] = 1
            else:
                target[i] += 1
            counter[i] = 0
        #用这个函数去判断现在窗口是否符合更新输出的条件，如果符合，
        #更新后去移动start,对窗口进行收缩
        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if counter[k] < target[k]:
                    return False
            return True

        for end in range(n):
            if s[end] in target:
                counter[s[end]] += 1
            while start < n and contains(counter, target):
                if end - start + 1 < min_len:
                    min_len = end-start+1
                    res = s[start:end + 1]
                if s[start] in target:
                    counter[s[start]] -= 1
                start += 1
        if min_len == float('inf'):
            return ""  
        else:
            return res
        
from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        min_len = float('inf')
        res = ''
        n = len(s)
        target = Counter(t)
        counter = defaultdict(lambda: 0)

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        for end in range(n):
            if s[end] in target:
                counter[s[end]] += 1
            while start < n and contains(counter, target):
                if end - start + 1 < min_len:
                    min_len = end-start+1
                    res = s[start:end + 1]
                if s[start] in target:
                    counter[s[start]] -= 1
                start += 1
        return "" if min_len == float('inf') else res