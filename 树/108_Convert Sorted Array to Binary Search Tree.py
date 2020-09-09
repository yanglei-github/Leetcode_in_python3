# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:04:04 2019

@author: leiya
"""

'''
0909
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        left_node = self.sortedArrayToBST(nums[:mid])
        right_node = self.sortedArrayToBST(nums[mid+1:])
        root.left = left_node
        root.right = right_node
        return root
    
'''
0703 updated
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root_index = len(nums) // 2
        root = TreeNode(nums[root_index])
        left_node = self.sortedArrayToBST(nums[:root_index])
        right_node = self.sortedArrayToBST(nums[root_index+1:])
        root.left = left_node
        root.right = right_node
        return root
    
    
#updated 0628
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #有序数组
        n = len(nums)
        if n < 1:
            return None
        root_index = n // 2
        root = TreeNode(nums[root_index])
        left_node = self.sortedArrayToBST(nums[:root_index])
        #注意这块需要root_index+1，因为不应该包括root节点了
        right_node = self.sortedArrayToBST(nums[root_index+1:])
        root.left = left_node
        root.right = right_node
        return root
    
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root   
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    
        def to_bst(nums,start,end):
            if start > end:
                return None
            mid = (start+end) // 2
            node = TreeNode(nums[mid])
            node.left = to_bst(nums,start,mid-1)
            node.right = to_bst(nums,mid+1,end)
            return node
        return to_bst(nums,0,len(nums)-1)