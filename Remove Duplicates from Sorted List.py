# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:06:05 2015

@author: ZSHU
"""

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=ListNode('s'); start=p; p.next=head 
        while head:
            if p.val!=head.val:
                p.next=head; head=head.next; p=p.next 
            else:
                head=head.next 
        p.next=head
        
        return start.next 