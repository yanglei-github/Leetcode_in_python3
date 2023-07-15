# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:49:25 2019

@author: leiya
"""
#0709 sliding window
'''
这道题的难点在于如果start,end从某个位置开始，可能会一直一样，这样在循环里可能没办法把这部分统计进去，
可以根据start,end最后是否重合来把这部分特殊情况解决掉
注意每次改变滑动窗口以后需要移动窗口指针
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(2,n+1):
            #每次要用新的new_res,start
            new_res = ''
            start = 0
            for end in range(len(res)):
                if res[end] != res[start]:
                    new_res += str(end-start) + res[start]
                    start = end
            if end != start:
                new_res += str(end-start+1) + res[start]
            else:
                new_res += '1' + res[end]
            res = new_res
        return res
    
    
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