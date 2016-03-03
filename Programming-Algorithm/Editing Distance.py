# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:43:04 2015

@author: ZSHU
"""
"""
dynamic programming
"""
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        
        if word1==word2:
            return 0
        if len(word1)==0:
            return len(word2)
        if len(word2)==0:
            return len(word1)
        
        dp=[[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for i in range(1,len(dp)): dp[i][0]=i
        for i in range(1,len(dp[0])):dp[0][i]=i
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[j-1]==word2[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[i][j]