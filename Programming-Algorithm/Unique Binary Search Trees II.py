# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:22:47 2015

@author: ZSHU
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def trees(vector):
            if len(vector)==0:
                return [None] # return a list strucure here 
            
            res=[]   
            for i in range(len(vector)):
                left=trees(vector[:i])
                right=trees(vector[i+1:])
         
                for node1 in left:
                    for node2 in right:
                        root=TreeNode(vector[i])
                        root.left=node1
                        root.right=node2
                        res.append(root)
            return res # immedidate return the results of eavh level
            
        return trees(range(1,n+1))