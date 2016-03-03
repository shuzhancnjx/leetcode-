# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:23:58 2015

@author: ZSHU
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        stack=[]; temp=head
        while temp:
            stack.append(temp)
            temp=temp.next
 
        p1,p2=0, len(stack)-1
        while p2-p1>=2:
            stack[p1].next=stack[p2]
            stack[p1].next.next=stack[p1+1]
            stack[p2-1].next=None
            p1+=1;p2-=1
 