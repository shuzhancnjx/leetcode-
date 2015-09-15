# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:19:40 2015

@author: ZSHU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nodes=[]
        while head:
            nodes.append(head.val)
            head=head.next 
        
        def toBST(nums):
            if len(nums)==0:
                return 
            
            loc=len(nums)/2
            root=TreeNode(nums[loc])
            root.left=toBST(nums[:loc])
            root.right=toBST(nums[loc+1:])
            return root
        
        return toBST(nodes)