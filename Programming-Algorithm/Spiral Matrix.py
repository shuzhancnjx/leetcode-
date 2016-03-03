# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 13:20:38 2015

@author: ZSHU
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]: 
            return []
            
        l, w=len(matrix[0])-1, len(matrix)-1
        circle1, circle2=len(matrix)/2, len(matrix[0])/2
        res,i=[],0
        
        while i<circle1 and i<circle2:
             for j in range(i, l-i+1): res.append(matrix[i][j])
             for j in range(i+1, w-i+1): res.append(matrix[j][l-i])
             for j in range(l-i-1, i-1,-1): res.append(matrix[w-i][j])
             for j in range(w-i-1, i, -1): res.append(matrix[j][i])
             i+=1
        
        if len(res)< (l+1)*(w+1): 
            if circle2>=circle1: res+=matrix[w/2][i:l-i+1]
            else:
                for k in range(i, w-i+1): res.append(matrix[k][l/2])
        
        return res 