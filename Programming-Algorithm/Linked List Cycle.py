# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:13:09 2015

@author: ZSHU
"""

"""
change the value of the list for labeling the "visited or not visited"
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        while head and head.next:
            if head.val=='v':
                return True 
            head.val='v'
            head=head.next 
        return False 
            