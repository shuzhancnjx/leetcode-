# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:59:05 2015

@author: ZSHU
"""

'''
another example of binary search 
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0; right=x
 
        while right>=left:
            if left**2==x: return left
            elif right**2==x: return right
            else:
                center=(left+right)/2
                if center**2==x: return center 
                elif center**2>x: right=center-1
                else: left=center+1
        return right             