# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:33:14 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        
        def kth(root, res,k):
            if len(res)==k:
                return 
            if root:
                kth(root.left, res, k)
                res+=[root.val]
                kth(root.right , res, k)
        res=[]
        kth(root, res, k)
        return res[k-1]