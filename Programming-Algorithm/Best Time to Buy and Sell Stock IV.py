# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:37:28 2015

@author: ZSHU
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k>len(prices)/2:
            profit,i=0,1
            while i<len(prices):
                profit += prices[i]-prices[i-1] if prices[i]-prices[i-1]>0 else 0
                i+=1
            return profit 
        
        
        dp=[None]*(2*k+1)
        dp[0]=0
        for i in range(len(prices)):
            for j in range(min(i+1, 2*k),0,-1):
                dp[j]=max(dp[j],dp[j-1]+prices[i]*[1,-1][j%2])
        return max(dp)