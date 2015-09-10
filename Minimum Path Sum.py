# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 15:20:30 2015

@author: ZSHU
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
                
        l=len(grid[0]); w=len(grid)
        dp=[[0 for i in range(l)] for j in range(w)]
        dp[0][0]=grid[0][0]
        
        for i in range(1, l):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        for i in range(1, w):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        
        for i in range(1, w):
            for j in range(1, l):
                dp[i][j]=grid[i][j]+min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]