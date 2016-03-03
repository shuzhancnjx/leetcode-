# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 14:41:46 2015

@author: ZSHU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        starting=p
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                p.next=l1; l1=l1.next
            elif l1.val>l2.val:
                p.next=l2; l2=l2.next
            p=p.next

        if l1!=None: p.next=l1
        elif l2!=None: p.next=l2

        return starting.next