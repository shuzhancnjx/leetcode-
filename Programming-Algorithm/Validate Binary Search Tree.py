# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:18:13 2015

@author: ZSHU
"""

'''
using the properties of the inorder trasversial
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, res=[], []
        
        while stack or root:
            if root:
                if stack and root.val>=stack[-1].val:
                    return False
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                if res and root.val<=res[-1]:
                    return False 
                res.append(root.val)
                root=root.right
        return True 