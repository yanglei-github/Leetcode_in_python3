# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:47:52 2019

@author: leiya
"""


'''
0901 updated
reversed返回的为对象地址，此处需要单独转换一步，sorted仍然返回的是对象本身，注意区别
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#广度优先搜索 BFS
'''bfs是用来搜索最短径路的解是比较合适的，比如求最少步数的解，
最少交换次数的解，因为bfs搜索过程中遇到的解一定是离最初位置最近的，
所以遇到一个解，一定就是最优解，此时搜索算法可以终止，而如果用dfs，
会搜一些其他的位置，需要搜很多次，然后还要一个东西来记录这次找的位置，之后找到的还要和这次找到的进行比较，这样就比较麻烦
dfs适合搜索全部的解，因为要搜索全部的解，在记录路径的时候也会简单一点，
而bfs搜索过程中，遇到离根最近的解，并没有什么用，也必须遍历完整棵搜索树。
bfs是浪费空间节省时间，dfs是浪费时间节省空间。因为dfs要走很多的路径，
可能都是没用的，（做有些题目的时候要进行剪枝，就是确定不符合条件的就可以结束，以免浪费时间，否则有些题目会TLE）；
而bfs可以走的点要存起来，需要队列，因此需要空间来储存，但是快一点。
'''

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            vals = []
            for _ in range(len(queue)):
                cur_node = queue.pop(0)
                vals.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(vals)
        
        #reversed返回的为对象地址，此处需要单独转换一步，sorted仍然返回的是对象本身，注意区别
        return list(reversed(result))


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        current_level = [root]
        while current_level:
            vals = []
            next_level = []
            for node in current_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            result.append(vals)
            current_level = next_level
        return list(reversed(result))
    
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result,current =[], [root]
        while current:
            next_level, vals = [],[]
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            current = next_level
            result.append(vals)
        return list(reversed(result))
    
