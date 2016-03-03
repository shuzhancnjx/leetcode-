# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 11:56:36 2015

@author: ZSHU
"""

"""
dynamic programming:

"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        
        l=len(matrix); w=len(matrix[0])
        dp=[[0 for i in range(w)] for j in range(l)]
        dp[0][0]=int(matrix[0][0])
        
        maxsquare=dp[0][0]
        for i in range(1, l): dp[i][0]=int(matrix[i][0]); maxsquare=max(maxsquare, dp[i][0])
        for i in range(1, w): dp[0][i]=int(matrix[0][i]); maxsquare=max(maxsquare, dp[0][i])
    
        
        for i in range(1, l):
            for j in range(1, w):
                if matrix[i][j]=='1': 
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                    maxsquare=max(maxsquare, dp[i][j])
        return maxsquare**2