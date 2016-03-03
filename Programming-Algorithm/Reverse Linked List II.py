# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 12:47:02 2015

@author: ZSHU
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p=ListNode(0)
        start=p
        p.next=head 
        p1=0
        
        while p1<m-1:
            head=head.next
            p=p.next
            p1+=1
        
        while p1<n-1:
            temp=head.next
            head.next=temp.next
            temp.next=p.next
            p.next=temp 
            p1+=1
        
        return start.next 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

