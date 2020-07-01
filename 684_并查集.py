# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:01:48 2020

@author: leiya
"""
#并查集可以动态地连通两个点，并且可以非常快速地判断两个点是否连通。
class disjoint:
    def __init__(self, N):
        self.array = [-1] * (N+1)
        
    def find_root(self, i):
        while self.array[i] != -1:
            i = self.array[i]
        return i
    
    def union(self, i, j):
        i = self.find_root(i)
        j = self.find_root(j)
        #node i, node j如果不相连那么就把他们连起来（通过把他们对应的root连起来，他们就相当于连起来了，我们令后面是前面的root）
        if i != j:
            self.array[i] = j
            # return j
        else:
            # return -1
            pass
    
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #这步循环目的在于找到不重复node的个数
        a = set()
        for i in edges:
            a.add(i[0])
            a.add(i[1])
            
        tree = disjoint(len(a))
        
        answer = []
        
        for i in edges:
            x, y = tree.find_root(i[0]), tree.find_root(i[1])
            #如果x,y的根一样，那么证明他们可以通过根相连，那么当前的边必定会形成环
            if x != y:
                tree.union(i[0], i[1])
            else:
                #如果此时查到他们相连，即root相同，那么说明前面已经可以通过root相连，这时候新加的这条边就构成了环
                answer = i
        
        return answer