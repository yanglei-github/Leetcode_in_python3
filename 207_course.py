# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:31:00 2020

@author: leiya
"""



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for node,node1 in prerequisites:
            indegrees[node] += 1
            #有向图邻接表，每个node的出边
            adjacency[node1].append(node)
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            pop_node = queue.pop(0)
            numCourses -= 1
            for next_node in adjacency[pop_node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)
        if numCourses == 0:
            return True
        else:
            return False
        
        
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        queue = []
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        while queue:
            pop_node = queue.pop(0)
            numCourses -= 1
            for node in adjacency[pop_node]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
            
        return not numCourses
    
    