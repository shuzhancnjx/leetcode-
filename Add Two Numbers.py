# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:08:22 2015

@author: ZSHU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        starting, carrier= p, 0
        
        while l1!=None and l2!=None:
            p.next=ListNode((l1.val+l2.val+carrier)%10)
            carrier=(l1.val+l2.val+carrier)/10
            l1=l1.next; l2=l2.next; p=p.next
        
        while l1!=None:
            p.next=ListNode( (l1.val+carrier)%10)
            carrier=(l1.val+carrier)/10
            l1=l1.next; p=p.next

        while l2!=None:
            p.next=ListNode( (l2.val+carrier)%10)
            carrier=(l2.val+carrier)/10
            l2=l2.next; p=p.next

        if carrier==1:
            p.next=ListNode(carrier)
        return starting.next