# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 15:03:57 2015

@author: ZSHU
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        w=len(obstacleGrid[0]); l=len(obstacleGrid)
        dp=[[0 for i in range(w)] for j in range(l)]
        
        for i in range(w):
            if obstacleGrid[0][i]!=1 and (i==0 or dp[0][i-1]==1): dp[0][i]=1
        for i in range(l):
            if obstacleGrid[i][0]!=1 and (i==0 or dp[i-1][0]==1):dp[i][0]=1
        
        for i in range(1, l):
            for j in range(1, w):
                dp[i][j]= 0 if obstacleGrid[i][j]==1 else dp[i-1][j]+dp[i][j-1]
        
        
        return dp[-1][-1]
