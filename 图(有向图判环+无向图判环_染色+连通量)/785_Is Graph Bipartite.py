# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:07:02 2020

@author: leiya
"""

'''
0709
从node0开始bfs一层一层的染色
0713
染色问题的输入应该规划化为邻接表的形式，注意这里的邻接表是无向图的邻接表，要区别于有向图的邻接表
20220304
标准无向图的染色问题，可通过547题巩固
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #相邻元素需要染上不同的颜色
        color = {}
        #for循环的作用是为了解决非连通图的问题
        for node in range(len(graph)):
            #可能存在不相连的独立节点或者独立的节点集，因此要遍历所有的nodes,保证所有nodes都可以上色，即图可能是不连通的
            if node not in color:
                queue = [node]
                color[node] = 0
                while queue:
                    '''
                    更宏观一点的理解为：queue中的node始终是染过色的node，因此在寻找该node相邻的node时候，对于染过色的相邻node无须再加入queue中
                    因为必然在前面的某一层中我们将该相邻node染色后加入到queue中，已经访问过了，没必要重新访问
                    '''
                    pop_node = queue.pop(0)
                    for next_node in graph[pop_node]:
                        #没染色就染上
                        if next_node not in color:
                            '''
                            queue.append(next_node)只能加在没有染色的判断里，不能拿出来
                            因为如果染完色了说明在当前层的前面的某一层遍历过了，因此不需要逆向重新遍历
                            '''
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

