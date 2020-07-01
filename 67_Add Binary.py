# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:53:44 2019

@author: leiya
"""

#1.str,int类型
#2.变量的声明
#3.while循环里变量每次循环的更新
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                temp1 = int(a[i])
            else:
                temp1 = 0
            
            if j >= 0:
                temp2 = int(b[j])
            else:
                temp2 = 0
            
            t = (temp1 + temp2 + carry) % 2
            carry = (temp1 + temp2 + carry) // 2
            res += str(t) 
            i -= 1
            j -= 1
        return res[::-1]




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aint = int(a,2) + int(b,2)
        return str(bin(aint))[2:]
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result,carry,val = "",0,0
        for i in range(max(len(a),len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry,val = val // 2,val%2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]
    
    
