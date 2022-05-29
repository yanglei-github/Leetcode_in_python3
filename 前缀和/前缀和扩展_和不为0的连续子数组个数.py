# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:08:24 2020

@author: leiya
"""

#和不为0的连续子数组个数
class Solution:
    def subarraySum(self, nums):
        adict = {}
        adict[0] = 1
        sum = 0
        count = 0
        for index,num in enumerate(nums):
            sum += num
            #这里的计数可以这样理解：1,2,3现在遍历到3了，正常来说多加一个3应该多加了3个连续子数组，[3],[2,3],[1,2,3]
            #可以从后向前数
            count += index+1
            #如果之前的和和现在的和一样的话，那么意味着现在的个数减去之前sum出现的个数，就可以得到不为0的个数，因为两者之间就是和为0的个数，
            #不然不会出现之前和为a,现在和还是a的情况，这就说明两者之间的部分的和是0
            if sum in adict.keys():
                count -= adict[sum]
            if sum not in adict:
                adict[sum] = 1
            else:
                adict[sum] += 1
        return count

solution = Solution()
res = solution.subarraySum([-1,0,1])
print(res)