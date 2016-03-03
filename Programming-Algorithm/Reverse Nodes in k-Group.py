# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 16:45:39 2015

@author: ZSHU
"""
"""
using stack to swap the nodes 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head 
        
        p=ListNode(0)
        start=p

        stack=[]
        while head!=None:
            i=0
            while head!=None and i<k:
                stack.append(head.val)
                head=head.next
                i+=1
        
            if len(stack)==k:
                while stack!=[]:
                    p.next=ListNode(stack.pop())
                    p=p.next 
            else:
                 while stack!=[]:
                     p.next=ListNode(stack.pop(0))
                     p=p.next 
                 break 
        return start.next 
