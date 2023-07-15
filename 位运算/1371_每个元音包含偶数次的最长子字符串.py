# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:55:59 2020

@author: leiya
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans, status, n = 0, 0, len(s)
        #记录的是这个status的长度
        pos = [-1] * (1 << 5)
        #全为偶数时置为0
        pos[0] = 0

        for i in range(n):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            if pos[status] != -1:
                ans = max(ans, i + 1 - pos[status])
            else:
                '''
                为了保证第一个字母是辅音字母时也可以输出正确的值，因为如果改为 pos[status] = i; 
                那相应的if语句要改为ans = max(ans, i - pos[status]);
                这样当第一个字母为辅音时，status = 0,~pos[status]判为真，ans就会被赋值为0，这显然不是正确的。
                同时题解中是用pos[atatus]是不是等于-1来判断前面是否出现过与status相同的奇偶性，所以也不能初始化为pos[0] = -1。
                就只好多加一个1
                '''
                pos[status] = i + 1
        return ans