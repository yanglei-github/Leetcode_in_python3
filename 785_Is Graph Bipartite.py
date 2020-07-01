# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:07:02 2020

@author: leiya
"""

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

