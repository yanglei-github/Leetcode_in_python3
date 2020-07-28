# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:32:20 2020

@author: leiya
"""



'''
0717
Note:无向图染色问题必须通过adjacency来解决
这道题是典型的无向图，可以理解为染色问题，找的就是有多少个独立的相连node构成的孤立图，但是这个孤立图不是直接体现在矩阵中的
（即这道题不是直接去判断给的图里有多少独立的1的区域）
直接体现在给的矩阵里的孤立图实际上就是独立岛屿的问题，这道题的难点在于需要根据他们的关系找到adjacency,之后通过adacency去自动判断孤立节点
adacency每次找一个node，然后根据adjacency把与他相连的node全都染上色（即标记），之后再去寻找其他独立的node
'''

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        row = len(M)
        adjacency = [[] for _ in range(row)]
        for i in range(row):
            for j in range(row):
                if i != j and M[i][j] == 1:
                    if j not in adjacency[i]:
                        adjacency[i].append(j)
                    if i not in adjacency[j]:
                        adjacency[j].append(i)
        count = 0
        used = [False for _ in range(row)]
        for node in range(row):
            if not used[node]:
                used[node] = True
                queue = [node]
                while queue:
                    pop_node = queue.pop(0)
                    for next_node in adjacency[pop_node]:
                        if not used[next_node]:
                            used[next_node] = True
                            queue.append(next_node)
                count += 1
        return count
    
    
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        color = {}
        row = len(M) 
        col = len(M)
        count = 0
        adjacency = [[] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i != j and M[i][j] == 1:
                    adjacency[i].append(j)
                    adjacency[j].append(i)
        for node in range(len(adjacency)):
            if node not in color:
                color[node] = node
                queue = [node]
                while queue:
                    pop_node = queue.pop(0)
                    for next_node in adjacency[pop_node]:
                        if next_node not in color:
                            #这块赋值意义不大，可以赋予任何值，只不过这里借助染色的思路标记node的使用情况，因此可以优化
                            color[next_node] = color[pop_node]
                            queue.append(next_node)    
                count += 1
        return count
    
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