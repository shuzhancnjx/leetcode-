# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 10:12:45 2015

@author: ZSHU
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix)<=1:
            return 
        
        circle=len(matrix)/2; l=len(matrix)-1
        
        for i in range(circle):
            for j in range(i, l-i):
                matrix[i][j], matrix[j][l-i], matrix[l-i][l-j], matrix[l-j][i]=\
                matrix[l-j][i], matrix[i][j], matrix[j][l-i], matrix[l-i][l-j]
        return 