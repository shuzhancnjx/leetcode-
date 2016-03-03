# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:24:53 2015

@author: ZSHU
"""

"""
classic example of dynamic programming
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        dp=[0]*(n+1); dp[1]=1; dp[2]=2
        
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]
            