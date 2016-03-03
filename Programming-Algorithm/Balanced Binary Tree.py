# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:55:04 2015

@author: ZSHU
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        
        
        def height(root,res,level):
            if root==None:
                res+=[level]
                return
            else:
                height(root.left, res, level+1)
                height(root.right, res, level+1)
                 
        def balanced(root):
            if root==None:
                return True 
            else:
                level, res=0,[]
                height(root.left, res, level+1)
                left, res=max(res), []
                right=height(root.right, res, level+1)
                right=max(res)
                if abs(left-right)<=1:
                    return balanced(root.left) and balanced(root.right)
                else:
                    return False 
        return balanced(root)

root=TreeNode(0)
root1=TreeNode(1)  
root2=TreeNode(2)  
root3=TreeNode(3)  
root4=TreeNode(4)  
root5=TreeNode(5)  
root6=TreeNode(6)  
root7=TreeNode(7)  

root.left=root1
root.right=root2

root1.left=root3
root1.right=root4

root3.left=root5
root3.right=root6
root5.left=root7

