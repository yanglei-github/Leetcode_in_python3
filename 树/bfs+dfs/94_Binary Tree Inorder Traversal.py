# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:30:53 2020

@author: leiya
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            #第一次弹出的实际上是一开始能找到的最左边的左节点，其实就是最后一个节点的根，然后判断这个根是否有右子树
            pop_node = stack.pop()
            res.append(pop_node.val)
            #cur每次初始化成一棵新树的root，然后根据while找到这棵新树的最左的左节点，同时把找的路径记录下来，记录方式就是把每个root记下来
            cur = pop_node.right
        return res
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            pop_node = stack.pop()
            res.append(pop_node.val)
            cur = pop_node.right
        return res
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res