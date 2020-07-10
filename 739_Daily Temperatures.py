# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:45:19 2020

@author: leiya
"""

'''
0701
一开始需要某个存储空间保留暂时找不到答案的元素内容,在下一次寻找是否满足过程中实际上存在判断的顺序，可以用stack来实现
0709
区分清楚stack和queue
'''

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(T))]
        for index in range(len(T)):
            while stack and T[index] > T[stack[-1]]:
                res[stack.pop()] = index - stack[-1]
            stack.append(index)
        return res
    
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        index_stack = [0]
        res = [0 for _ in range(len(T))]
        for i in range(1, len(T)):
            #注意stack需要判断特殊情况，如果stack一开始是空，会造成out of range
            while index_stack and T[index_stack[-1]] < T[i]:
                res[index_stack.pop()] = i - index_stack[-1]
            #每次判断完小loop后需要将当前value对应的index加入stack中
            index_stack.append(i)
        return res
    
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #单调递减栈
        stack = []
        res = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                res[stack.pop()] = i - stack[-1]
            #无论何种情况都应该加入到栈中
            stack.append(i)
        return res
    
    
    
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        l = len(T)
        stack = []    #这里定义一个栈就不用说了
        res = [0] * l   # 这里是最后要返回的result，因为题目中说没有匹配的就返回0，
                        # 所以这里初始化一个全是0的list，然后把那些有匹配的替换掉即可。

        for idx, t in enumerate(T):  # 下面是关键
            while stack and t > T[stack[-1]]:  # 当stack为空时，运行stack.append(idx)，则stack=[0]
                                                # 然后仅当遍历元素 t 小于stack顶端的值时append进去，
                                                # 这会导致stack中idx代表的元素是单调递减的，
                                                # 如果此时遍历到一个 t，大于stack顶端的值，那这个t就是离stack
                                                # 顶端值最近的那个大值。
                res[stack.pop()] = idx-stack[-1] # 然后pop出来，还是要注意stack.pop出来的是idx，这样res这
                                                 # 一串0里对应位置的0就会被替换成应有的值。                                        
                                                # 再进入while循环判断t和stack.pop后的新的顶端值哪个大。
                                                # 如此反复。
            stack.append(idx)
        return res