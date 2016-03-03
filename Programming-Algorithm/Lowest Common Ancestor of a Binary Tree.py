# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 11:14:54 2015

@author: ZSHU
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def path(root):
            if root==None or root==p or root==q:
                return root 
            left=path(root.left)
            right=path(root.right)
            
            if left and right: 
                return root
            return left or right
 
        return path(root)

"""
TLEd
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def intree(root, node):
            if root==node:
                return True 
            elif root==None:
                return False
            else:
                if intree(root.left, node) or intree(root.right, node):
                    return True 
                return False 
        def common(root):
            if root:
                if (intree(root.left, p) and intree(root.right, q)) or (intree(root.left, q) and intree(root.right, p)):
                    return root
                elif intree(root.left, p):
                    return common(root.left)
                return common(root.right)

        return common(root)
       