# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:44:16 2015

@author: ZSHU
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if A>=G or E>=C or B>=H or F>=D:
            return (C-A)*(D-B)+(G-E)*(H-F)
            
        return (C-A)*(D-B)+(G-E)*(H-F)-(min(G, C)-max(A, E))*(min(H, D)-max(B, F))