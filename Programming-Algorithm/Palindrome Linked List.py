# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:19:24 2015

@author: ZSHU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        
        p1,p2=0,len(stack)-1
        while p2>p1:
            if stack[p1].val==stack[p2].val:
                p1+=1;p2-=1
            else:
                return False 
        return True 