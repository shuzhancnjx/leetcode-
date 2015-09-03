# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 13:23:09 2015

@author: ZSHU
"""

"""
put the head.next at the very begining of the list
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        start=p
        p.next=head 
        
        if head==None:
            return head 
        
        while head.next!=None:
            temp=head.next 
            head.next=temp.next 
            temp.next=p.next 
            p.next=temp
        return start.next 



