# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:10:10 2015

@author: ZSHU
"""
"""
thanks the comments from 
http://www.cnblogs.com/zuoyuan/p/3701877.html
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return 
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow==fast: break 
        
        if slow==fast: 
            slow=head
            while slow!=fast:
                slow=slow.next; fast=fast.next
            return slow
        return 