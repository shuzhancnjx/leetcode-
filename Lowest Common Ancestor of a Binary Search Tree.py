# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:56:28 2015

@author: ZSHU
"""
"""
this is the solution for the binary SEARCH tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if (root.val<=p.val and root.val >=q.val) or (root.val<=q.val and root.val>=p.val):
            return root
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        