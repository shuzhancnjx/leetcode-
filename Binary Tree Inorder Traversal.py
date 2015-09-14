# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:55:40 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res=[], []
        
        while stack or root: 
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res