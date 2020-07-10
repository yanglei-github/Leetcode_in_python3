# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:07:02 2020

@author: leiya
"""

'''
0709
从node0开始bfs一层一层的染色
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #相邻元素需要染上不同的颜色
        color = {}
        for node in range(len(graph)):
            #可能存在不相连的独立节点或者独立的节点集，因此要遍历所有的nodes,保证所有nodes都可以上色
            if node not in color:
                queue = [node]
                color[node] = 0
                while queue:
                    pop_node = queue.pop(0)
                    for next_node in graph[pop_node]:
                        #没染色就染上
                        if next_node not in color:
                            queue.append(next_node)
                            color[next_node] = color[pop_node] ^ 1
                        #染过色了就判断一下染的对不对
                        elif color[next_node] == color[pop_node]:
                            return False
        return True
    
    
class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                queue = [node]
                color[node] = 0
                while queue:
                    node = queue.pop(0)
                    for nei in graph[node]:
                        if nei not in color:
                            queue.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

    
    
class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in xrange(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

