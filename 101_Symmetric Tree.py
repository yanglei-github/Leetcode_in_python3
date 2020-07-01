# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:25:36 2019

@author: leiya
"""



'''
updated 0626
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(left,right):
            if not left and not right:
                return True
            if not left and right or not right and left:
                return False
            if left.val == right.val:
                return isSame(left.left,right.right) and isSame(left.right,right.left)
            else:
                return False
        if not root:
            return True
        return isSame(root.left,root.right)

#迭代版，实际上就是在bfs弹出nodes的时候进行判断
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append((root, root))
        while queue:
            left, right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True

#------------------------------------------------------------------------------

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def isSym(L, R):
            if L is None and R is None:
                return True
            if L and R:
                return L.val == R.val and isSym(L.left, R.right) and isSym(L.right, R.left)

            else:
                return False
#此处必须加一个return,如果不加return的话即使isSym有return值也不会作为isSymmetric的return返回出去
        return isSym(root, root)
    
    
    
class Solution:
    def isSymmetric(self, root):
        def isSym(L,R):
            if L and R: 
                return L.val == R.val and isSym(L.left, R.right) and isSym(L.right, R.left)
            else:
                return L == R
        return isSym(root, root)
    '''   def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)'''
    
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isSymmetric_twovariable(root.left,root.right)
        
    def isSymmetric_twovariable(self,left,right):
        if left and right:
            return left.val == right.val and self.isSymmetric_twovariable(left.left,right.right) and self.isSymmetric_twovariable(left.right,right.left)
        else:
            return left == right
        
    
    
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetricRecu(root.left,root.right)
    
    def isSymmetricRecu(self,left,right):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            return left.val == right.val and self.isSymmetricRecu(left.left,right.right) and self.isSymmetricRecu(left.right,right.left)
        else:
            return False