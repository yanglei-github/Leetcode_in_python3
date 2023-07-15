# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:43:06 2019

@author: leiya
"""

class Solution:
    #list中每项是整数时，必须转换成str形式才可以将List用join方式变为str形式
    def plusOne(self, digits: List[int]) -> List[int]:
        alist = []
        newdigits = list(map(str,digits))
        aint = int(''.join(newdigits)) + 1
        for i in str(aint):
            alist.append(int(i))
        return alist
    
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


class Solution:
    def plusOne(self, digits):
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                print(digits)
            
        digits.insert(0,1)
        return digits
solution = Solution()
solution.plusOne([9,9])
