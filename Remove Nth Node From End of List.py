# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 12:29:38 2015

@author: ZSHU

"""
logically easy, but pay attention to the special case with n=1. 
"""
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n==0:
            return head 
            
        stack=[]
        while head!=None:
            stack.append(head)
            head=head.next
        
        if len(stack)<n:
            return stack[0]
        elif len(stack)==n:
            if n==1:
                return None 
            return stack[1]
        else:
            if n==1:
                stack[-2].next=None 
                return stack[0]
                
            stack[-(n+1)].next=stack[-(n-1)]
            return stack[0]