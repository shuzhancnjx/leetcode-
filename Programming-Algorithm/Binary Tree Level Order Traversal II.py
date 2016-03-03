# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:10:15 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def level(root, levels, res):
            if root:
                if levels>len(res):
                    res+=[[]]*(levels-len(res))
                
                res[levels-1].append(root.val)
                
                level(root.left, levels+1, res)
                level(root.right, levels+1, res)
        
        if root==None:
            return []
        res=[[]]
        level(root, 1, res)
        return res[::-1]