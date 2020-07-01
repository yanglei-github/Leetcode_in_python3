# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:49:25 2019

@author: leiya
"""

#updated 0629 这道题只能通过j与j+1比较，有题目本身的特性决定，每次通过小循环找到重复数字的个数
class Solution:
    def countAndSay(self, n: int) -> str:
        temp = '1'
        for i in range(n-1):
            j = 0
            newtemp = ''
            while j < len(temp):
                count = 1
                while j < len(temp) - 1 and temp[j] == temp[j+1]:
                    count += 1
                    j += 1
                newtemp += str(count) + temp[j]
                j += 1
            temp = newtemp
        return temp

class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for i in range(n-1):
            seq = self.getNext(seq)
        return seq
    def getNext(self,seq):
        i,next_seq = 0
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i+1]:
                count += 1
                i += 1
            next_seq += str(count) + seq[i]
            i += 1
        return nex_seq