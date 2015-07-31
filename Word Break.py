# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:12:00 2015

@author: ZSHU
"""
 
"""
thanks the comments from http://www.cnblogs.com/zuoyuan/p/3760660.html
""" 
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        
        dp=[False for i in xrange(len(s)+1)]
        dp[0]=True 
        
        for i in range(1, len(s)+1):
            for j in range(i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True 
        
        return dp[-1]