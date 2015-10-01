# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:58:22 2015

@author: ZSHU

"""

"""
a level ordering 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def level(lev, res, root):
            if root:
                if lev>len(res):
                    res+=[[]]*(lev-len(res))
                res[lev-1]+=[root.val]
                level(lev+1, res, root.left)
                level(lev+1, res, root.right)
        if root==None:
            return []
            
        temp=[[root.val]]; tem=[]
        level(1, temp, root)
        for i in range(len(temp)):
            tem.append(temp[i][-1])
        return tem
