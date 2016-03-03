# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:39:16 2015

@author: ZSHU
"""

"""
dp programming
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)<2:
            return triangle[0][0]
        
        i=len(triangle)-2
        while i>=0:
            
            for j in range(len(triangle[i])):
                triangle[i][j]= min(triangle[i][j]+triangle[i+1][j], triangle[i][j]+triangle[i+1][j+1])
            i-=1
                
        return triangle[0][0]   