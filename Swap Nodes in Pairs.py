# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 16:38:47 2015

@author: ZSHU
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head 
        
        p=ListNode(0)
        starting=p

        while head!=None and head.next!=None:
            temp=head.next
            head.next=temp.next
            temp.next=head
            p.next=temp 
    
            head=head.next
            p=p.next.next
        return starting.next
