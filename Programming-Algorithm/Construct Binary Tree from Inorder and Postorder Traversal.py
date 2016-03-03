# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:35:38 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return
        temp=postorder.pop()
        root=TreeNode(temp)
        index=inorder.index(temp)
        
        root.right=self.buildTree(inorder[index+1:], postorder)
        root.left=self.buildTree(inorder[:index], postorder)
        return root