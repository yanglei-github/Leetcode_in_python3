# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:14:10 2020

@author: leiya
"""


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [0] * 2
            '''
            le_0表示对于左子树，不偷左子树的根，le_1表示对于左子树，偷其根
            '''
            '''
            相当于每次把子树中的最大值传回上层树，dp的思想
            '''
            le_0,le_1 = dfs(root.left)
            ri_0,ri_1 = dfs(root.right)
            off_root = max(le_1+ri_1,le_0+ri_0,le_1+ri_0,le_0+ri_1)
            on_root = le_0+ri_0+root.val
            return [off_root,on_root]
        return max(dfs(root))