# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:36:37 2015

@author: ZSHU
"""

"""
dynamic programming like climbing stairs; but pay attention to cases with "0"
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if s[0]=='0':
            return 0
        
        dp=[0]*(len(s)+1)
        dp[0]=1; dp[1]=1
 
        for i in range(1, len(s)):
            if s[i-1]!='0' and s[i]!='0':
                if int( s[i-1:i+1]  )<=26:
                    dp[i+1]=dp[i-1]+dp[i]
                else:
                    dp[i+1]=dp[i]
            elif s[i]=='0' and s[i-1]=='0':
                return 0
            elif s[i-1]=='0':
                dp[i+1]=dp[i]
            elif s[i]=='0':
                if int(s[i-1:i+1])<=26: dp[i+1]=dp[i-1]
                else: return 0

        return dp[-1]