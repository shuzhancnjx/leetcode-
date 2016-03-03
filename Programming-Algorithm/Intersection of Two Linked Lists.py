# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:44:39 2015

@author: ZSHU
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA=0; lenB=0; tempA=headA; tempB=headB
        while headA or headB:
           if headA:
               lenA+=1;headA=headA.next 
           if headB:
               lenB+=1; headB=headB.next 
        
        diff=lenA-lenB
        while tempB:
            while abs(diff)>0:
                if diff>0:
                    diff-=1
                    tempA=tempA.next
                else:
                    diff+=1
                    tempB=tempB.next 
            if tempB==tempA:
                return tempB
            tempA=tempA.next; tempB=tempB.next 
        return 