# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:10:32 2015

@author: ZSHU
"""

"""
bit compuation, >> and ^
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(2**n):
            res.append( (i>>1)^i)
        return res