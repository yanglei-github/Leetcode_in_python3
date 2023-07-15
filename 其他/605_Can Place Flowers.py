# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:02:22 2020

@author: leiya
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i+1 == len(flowerbed) or flowerbed[i+1] == 0):
                #if i + 1 == len(flowerbed):
                    #if flowerbed[0] == 1:
                        #break
                flowerbed[i] = 1
                count += 1
        return count == n
