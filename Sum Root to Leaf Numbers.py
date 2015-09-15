# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:35:13 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def paths(path, root, res):
            if root.left==None and root.right==None:
                res.append(int(path))
            else:
                if root.left:
                    paths(path+str(root.left.val), root.left,res)
                if root.right:
                    paths(path+str(root.right.val), root.right, res)
        res=[]
        if root:
            paths(str(root.val), root, res)
        return sum(res)