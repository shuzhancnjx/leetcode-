# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 13:20:24 2015

@author: ZSHU
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1,p2=1,n
        
        
        while p1<=p2:
            mid=(p1+p2)/2
            if isBadVersion(mid):
                p2=mid-1
            else:
                p1=mid+1
        return p1