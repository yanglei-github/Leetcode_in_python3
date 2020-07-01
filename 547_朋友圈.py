# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:32:20 2020

@author: leiya
"""

#---------------------还可以用并查集做，待补充-----------------------------
#需要引入visited数组来记录node是否已经被访问过了，访问过的节点需要及时标记
#BFS:将grid视为邻接表，row为每个node
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        visited = [False for _ in range(len(M))]
        for i in range(len(M)):
            if not visited[i]:
                visited[i] = True
                queue = [i]
                while queue:
                    pop_node = queue.pop(0)
                    for j in range(len(M)):
                        if not visited[j] and M[pop_node][j] == 1:
                            visited[j] = True
                            queue.append(j)
                res += 1
        return res
    
    
#DFS:将grid视为邻接表，row为每个node
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        res = 0
        visited = [False for _ in range(len(M))]
        for i in range(len(M)):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1
        return res