# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:40:14 2020

@author: leiya
"""




'''
0630:本题需要注意三点
1.小循环中需要添加low < high
2.s.lower()有返回值，如果不赋值，那么s没有变化
3.isdigit(),isalpha(),isalnum()
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers
        if not s:
            return True
        low = 0
        high = len(s)-1
        s = s.lower()
        while low < high:
            #一旦有while注意每次loop中更新low和high
            while low < high and not s[low].isdigit() and not s[low].isalpha():
                low += 1
            while low < high and not s[high].isdigit() and not s[high].isalpha():
                high -= 1
            
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False
        return True
#isdigit,isalpha,isalnum
#双指针，判断当前位置是否为字母或者数字，如果不是就跳过
#0619 updated:需要认真思考while中判断的顺序，应该是分别判断low,high对应的位置是否符合条件，
#如果不符合条件那么跳出循环重新去找，知道找到两者都符合条件时再继续往下找
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                continue
            if not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
#isalnum()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < len(s) and j >= 0:
            if not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                continue
            if not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        if i != len(s) and j != -1:
            return False
        else:
            return True
        

        