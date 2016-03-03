# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:18:37 2015

@author: ZSHU
"""

'''
introduce a variable 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p=ListNode(0); start=p; p.next=head
        
        while head and head.next: 
            if head.val<x:
                if p.next==head: 
                    p=p.next; head=head.next 
            else:
                move=head.next
                while move and move.val>=x:
                    move=move.next; head=head.next 
                if move: 
                   head.next=move.next
                   move.next=p.next; p.next=move; p=p.next 
        return start.next
    
