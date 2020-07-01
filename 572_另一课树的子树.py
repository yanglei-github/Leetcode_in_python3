# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:59:59 2020

@author: leiya
"""

#based on 100.The Same Tree
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSametree(s,t):

            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val == t.val:
                return isSametree(s.left,t.left) and isSametree(s.right, t.right)
            else:
                return False
        
        if not s and not t:
            return True
        if not s or not t:
            return False 
        else:
            return isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)