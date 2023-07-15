# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:16:02 2019

@author: leiya
"""
#split()的时候，多个空格当成一个空格；split() = 'a ' --- ['a']
#split(' ')的时候，多个空格都要分割，每个空格分割出来空。split(' ') = 'a ' --- ['a','']
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split() 
        if len(s) == 0:  
            #s == []
            return 0
        else :
            return len(s[-1])
        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if ' ' not in s:
            return len(s)
        count = 0
        length = 0
        for i in range(len(s)):
            if s[i] == ' ':
                
                
                count = 0
            else:
                count += 1
                length = count
        return length

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        local_count = 0
        if ' ' not in s:
            return len(s)
        
        for i in range(len(s)):
            if s[i] == ' ':
                
                local_count = 0
                
            else:
                local_count += 1
                count = local_count
        return count