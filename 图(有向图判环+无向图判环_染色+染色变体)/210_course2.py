# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:50:52 2020

@author: leiya
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        res = []
        for node,node1 in prerequisites:
            indegrees[node] += 1
            adjacency[node1].append(node)
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            pop_node = queue.pop(0)
            res.append(pop_node)
            numCourses -= 1
            for next_node in adjacency[pop_node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)
        if numCourses == 0:
            return res
        else:
            return []