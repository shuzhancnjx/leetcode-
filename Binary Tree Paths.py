# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:34:08 2015

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
    # @return {string[]}
    def binaryTreePaths(self, root):
        
        def path(root, res, pa):
            if root.left==None and root.right==None:
                res.append("->".join(pa))
                return 
            else:
                if root.left: 
                    path(root.left, res, pa+[str(root.left.val)])
                if root.right:
                    path(root.right, res, pa+[str(root.right.val)])
        
        if root==None: 
            return []
        res=[]
        path(root, res, [str(root.val)])
        return res 