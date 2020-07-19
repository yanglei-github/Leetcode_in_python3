# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:17:24 2020

@author: leiya
"""

'''
0712
这道题在滑动窗口中稍微有些特殊
我们说过，尽量将对输出的更新放到小循环外面，即尽量不要在缩小窗口的时候更新输出，以防特殊情况
但是这道题需要将更新放入小循环中，因为只有在小循环中才能找到需要更新的精确数值，一旦出了小循环，就不是如何要求的输出值了
在这道题里就是出了小循环，该滑动窗口和<s，不满足更新输出值的要求，这道题可以和904水果题类比
水果题进入小循环是不符合要求，这道题是进入小循环符合要求，要在符合要求的基础上看看有没有最优解，因为我们是默认移动end的，所以
这两道题的性质决定了更新输出值的位置，但我们仍要尽力将其放到while外面，这道题不在外面无关紧要，因为只有进入循环以后才可能有解
不在循环内的时候不需要更新解，即使一直没有进入内循环，我们也可以通过if min_len == float('inf')来解决特殊情况

0718:这道题还需要明确一点，即该题的窗口也无须回缩(回缩是指start前进的时候，end回缩去比较这个窗口，但在这道题里也不需要去比较这个窗口)
     原因在于一开始[start:end]肯定是sum_ < s了，end才会向后移动一位，[start:new_end],当start前进时[start+1:end](由new_end回缩回end),这个窗口是
     一开始[start:end]的子集，大窗口的和dou < s，更不用说他的子集了，因此回缩在这道题里没有意义，无须比较，这一点看似写题时候无关紧要，但是一定要
     判断清楚再去写，这是这道题之所以这么写的本质
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #sum_>=s的时候可以收缩窗口，这就是我们要找的while条件，因为
        #窗口不定长，所以用while，典型的不定长滑动窗口
        start = 0
        min_len = float('inf')
        sum_ = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            while sum_ >= s:
                min_len = min(min_len,end-start+1)
                sum_ -= nums[start]
                start += 1
            
        if min_len == float('inf'):
            return 0
        else:
            return min_len