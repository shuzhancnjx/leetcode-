# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:47:13 2015

@author: ZSHU
"""
"""
operation on the linked list
introducing the varialbe 'move' for removing all the duplicate components
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p=ListNode(0); start=p; p.next=head
        while head and head.next:
            if head.val!=head.next.val:
                p=p.next; head=head.next
            else:
                move=head
                while move and head.val==move.val:
                    move=move.next 
                head=move; p.next=head 
        return start.next 