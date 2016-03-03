# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:00:01 2015

@author: ZSHU
"""

"""
a simple algorithm based on the wiki. 
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        for i in xrange(1, n):
            if 5**i<=n:
                res+= (n/5**i)
            else:
                return res 
        return res 