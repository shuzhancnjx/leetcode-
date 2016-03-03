# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:51:06 2015

@author: ZSHU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start=ListNode(0); p=start; p.next=head
        while head: 
            if head.val==val: 
                p.next=head.next
            else:
                p=p.next
            head=head.next 
        return start.next
                