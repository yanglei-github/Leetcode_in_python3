# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:15:40 2020

@author: leiya
"""

#注意最后的结果是每个node中的val，不是node本身
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        cur_queue = [root]
        
        while cur_queue:
            cur_res = []
            next_queue = []
            for node in cur_queue:
                cur_res.append(node.val)
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)
            cur_queue = next_queue
            res.append(cur_res)
        return res
    
#方法二，更普遍
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #两种方式
        res = []
        if not root:
            return res
        cur_queue = [root]
        while cur_queue:
            current_len = len(cur_queue)
            cur_res = []
            for i in range(current_len):
                node = cur_queue.pop(0)
                cur_res.append(node.val)
                if node.left is not None:
                    cur_queue.append(node.left)
                if node.right is not None:
                    cur_queue.append(node.right)
            res.append(cur_res)
           
        return res