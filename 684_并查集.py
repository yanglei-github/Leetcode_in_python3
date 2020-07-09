# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:01:48 2020

@author: leiya
"""


'''
Caution:dsu只针对于无向图是否有环，有向图无法使用dsu
0709
1.注意引用新的类中的变量或者函数的时候，与要用class.var/func进行引用
2.DSU使用时应该看出node是否从1开始计数，从1计数，一开始初始化的时候需要传入node_nubmers+1，从0开始则直接传入node_numbers
3.一开始初始化dsu的时候需要传入node_numbers
'''

class DSU:
    def __init__(self, node_numbers):
        self.nodes_relation = [-1 for _ in range(node_numbers+1)]
    def root_find(self, node):
        while self.nodes_relation[node] != -1:
            node = self.nodes_relation[node]
        return node
    #此处可以无须写node_connection这个函数
    def node_connection(self, node1, node2):
        node1_root = self.root_find(node1)
        node2_root = self.root_find(node2)
        if node1_root != node2_root:
            self.nodes_relation[node1_root] = node2_root
        return
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #有一条冗余的链接，可以一条边一条边的进行判断，当发现这条边是想要链接的两个点已
        #经通过跟节点相连了，那么就没有必要链接他们了
        a = set()
        for i in edges:
            a.add(i[0])
            a.add(i[1])
        dsu = DSU(len(a))
        res = []
        for node1,node2 in edges:
            node1_root = dsu.root_find(node1)
            node2_root = dsu.root_find(node2)
            if node1_root != node2_root:
                dsu.nodes_relation[node1_root] = node2_root
            else:
                res = [node1,node2]
        return res 
    
    
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