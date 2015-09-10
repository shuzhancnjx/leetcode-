# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 13:43:33 2015

@author: ZSHU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0:
            return head

        
        p=ListNode(0); p.next=head;start=p; count=0
        while p.next:
           count+=1
           p=p.next 
        
        move=count-(k%count); p.next=start.next 
        for i in range(0, move):
            p=p.next 
        head=p.next; p.next=None
        
        return head 


