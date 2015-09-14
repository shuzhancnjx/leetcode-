# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:48:33 2015

@author: ZSHU
"""

 class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        
        dp=[0]*(n+1); dp[0]=1;dp[1]=1
        
        for i in range(2,n+1):
            for tem in range(i):
                dp[i]+=dp[tem]*dp[i-tem-1]
        return dp[-1]