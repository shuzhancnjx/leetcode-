# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:17:04 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return 
        loc=len(nums)/2
        root=TreeNode(nums[loc])
        root.left=self.sortedArrayToBST(nums[:loc])
        root.right=self.sortedArrayToBST(nums[loc+1:])
        return root