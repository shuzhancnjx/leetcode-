# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:25:05 2015

@author: ZSHU
"""

"""
the same idea of the inorder traversal 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]; res=[]
        while stack or root:
            if root: 
                stack.append(root)
                res.append(root.val)
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return res