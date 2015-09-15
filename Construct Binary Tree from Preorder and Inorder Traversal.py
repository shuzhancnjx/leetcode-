# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:27:16 2015

@author: ZSHU
"""

"""
solution I: recursive 
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
            if len(pre)==0:
                return None 
         
            root=TreeNode(pre[0])
     
            i=0
            while inorder[i]!=pre[0]:
                i+=1
         
            root.left=build(pre[1:i+1], inorder[:i])
            root.right=build(pre[i+1:], inorder[i+1:])
            return root
        
        return build(preorder, inorder)