# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:41:07 2015

@author: ZSHU
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x<0:
            sign=-1
            x=sign*x
        
        num=0 
        while x/10>0:
            num=num*10+x%10
            x=x/10
        num=num*10+x
        
        if num< -2**31 or num>2**31:
            return 0
        return sign*num