# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:35:58 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pre, inorder):
            if len(inorder)==0:
                return  
         
            root=TreeNode(pre[0])
            index=inorder.index(pre[0])
            pre.pop(0)
            
            root.left=build(pre, inorder[:index])
            root.right=build(pre, inorder[index+1:])
            return root
        
        return build(preorder, inorder)