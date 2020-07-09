# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:36:22 2020

@author: leiya
"""


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        count = 0
        res = []
        if not root:
            return res
        
        queue = [root]
        while queue:
            count += 1
            cur_res = []
            current_len = len(queue)
            for _ in range(current_len):
                pop_node = queue.pop(0)
                cur_res.append(pop_node.val)
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            if count % 2 == 0:
                res.append(cur_res[::-1])
            else:
                res.append(cur_res)
        return res