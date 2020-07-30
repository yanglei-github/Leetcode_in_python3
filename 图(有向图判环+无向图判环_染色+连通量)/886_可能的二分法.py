# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:25:07 2020

@author: leiya
"""

'''
这道题最重要的知识在于对图的理解
节点间关系平等，因此是无向图，无向图的邻接表必须清楚的找到所有与该节点相连的node
而有向图的邻接表只需要找到该节点的出node，这是两者很大的区别
此外，无向图有无环可用并查集判断，有向图有无环可用拓扑排序（邻接表+入度表）判断
0729: 需要留意node从0还是从1开始计数
'''
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        #bfs+color
        color = {}
        adjacency = [[] for _ in range(N+1)]
        for node1,node2 in dislikes:
            if node1 not in adjacency[node2]:
                adjacency[node2].append(node1)
            if node2 not in adjacency[node1]:
                adjacency[node1].append(node2)
        for node in range(1, len(adjacency)):
            if node not in color:
                color[node] = 0
                queue = [node]
                while queue:
                    pop_node = queue.pop(0)
                    for next_node in adjacency[pop_node]:
                        if next_node not in color:
                            color[next_node] = color[pop_node] ^ 1
                            queue.append(next_node)
                        elif color[next_node] == color[pop_node]:
                            return False
        return True

