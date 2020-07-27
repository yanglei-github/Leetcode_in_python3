# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:57:39 2020

@author: leiya
"""

#split() 方法将单词间的 “多个空格看作一个空格” 
class Solution:
    def reverseWords(self, s: str) -> str:
        nums = s.split()
        return ' '.join(nums[::-1])
    
    
#双指针后序遍历
#str.strip()可以去除字符串前后的空格
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': 
                i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ':
                i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回

