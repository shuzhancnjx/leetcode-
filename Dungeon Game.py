# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:33:47 2015

@author: ZSHU
"""

class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        if len(dungeon)==0:
            return 1
        
        row,col=len(dungeon),len(dungeon[0])
        dp=[[0 for i in range(col)] for j in range(row)]
        dp[row-1][col-1]=max(1-dungeon[row-1][col-1],1)
        
        for i in range(row-2, -1, -1):
            dp[i][col-1]=max(dp[i+1][col-1]-dungeon[i][col-1],1)
        for i in range(col-2,-1,-1):
            dp[row-1][i]=max(dp[row-1][i+1]-dungeon[row-1][i],1)
        
        for i in range(row-2,-1,-1):
            for j in range(col-2,-1,-1):
                dp[i][j]=min(max(dp[i+1][j]-dungeon[i][j],1), 
                             max(dp[i][j+1]-dungeon[i][j],1))
        return dp[0][0]