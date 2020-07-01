# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:11:33 2020

@author: leiya
"""
#0624
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        mark = set()
        right = 0
        for i in range(len(s)):
            if i != 0:
                #注意这里是i-1，排除当前位置的前一个位置的元素
                mark.remove(s[i-1])
            while right < len(s) and s[right] not in mark:
                mark.add(s[right])
                right += 1 
            length = max(length, right-i)
        return length
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        length = 0
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                length = max(length,right-left)
            else:
                left += 1
        return length
    
#0623 updated without flags
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        start = 0
        count = 1
        res = 1
        end = 1
        while end < len(s):
            for i in range(start,end):
                if s[i] == s[end]:
                    res = max(res, end-start)
                    start = i + 1
                    break
            res = max(res, end-start+1)
            end += 1
            
        return res
    
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        start = 0
        res = 0 
        flag = 0
        for i in range(1, len(s)):
            temp = start#注意这个赋值的位置，要在while外
            while start < i: 
                if s[start] != s[i]:
                    start += 1
                    
                else:
                    flag = 1
                    start += 1
                    break#结束任务后果断break
            if flag == 0:
                start = temp
            flag = 0#flag每次要重新置零
            res = max(res, i-start+1)
        return res
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        start = 0
        cur = 0
        length = 0
        flag = 0
        for i in range(1,len(s)):
            cur = start
            while start < i:
                if s[i] == s[start]:
                    length = max(length, i-start)
                    flag = 1
                    break
                else:
                    start += 1
            if flag == 0:
                start = cur
                length = max(length, i-start+1)
            else:
                start += 1
                flag = 0
        return length
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        start = 0
        end = 1
        res = 0
        flag = 0
        while end < len(s):
            cur = start
            while start < end:
                if s[start] == s[end]:
                    res = max(res, end-start)
                    flag = 1
                    break
                else:
                    start += 1
            if flag == 0:
                start = cur
                res = max(res, end-start + 1)
            else:
                start += 1
                flag = 0
                
            end += 1
        return res
    
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

