# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:50:01 2015

@author: ZSHU
"""

"""
based on iteration
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack=[]
        while stack or root:
            if root: 
                if root.right: 
                    stack.append(root.right)
                    
                if root.left: 
                    root.right=root.left
                    root.left=None
                else:
                    if stack:
                        root.right=stack.pop()
                root=root.right
    