# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:03:48 2015

@author: ZSHU
"""

'''
dynamic programming: 

1. the jth component of dp is to store the minimum cut in the string s[:j]
2. the variable palin is a two-dimensional variable. Palin[j][i] is to label if the s[j:i+1] is a palindrome
'''
            
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[len(s)]*(len(s)+1); dp[0]=-1; dp[1]=0; par=[0]
        palin=[[True for i in range(len(s))] for j in range(len(s))]

        i=1
        while i<len(s):
            dp[i+1]=dp[i]+1
            for j in range(0,i):
                if s[j]==s[i] and palin[j+1][i-1]:
                    dp[i+1]=min(dp[i+1],dp[j]+1)
                else:
                    palin[j][i]=False
            i+=1
        return dp[-1]

"""
the solution TLEd.
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPalin(s):
            p1,p2=0, len(s)-1
            while p2>p1:
                if s[p1]==s[p2]:
                    p1+=1;p2-=1
                else:
                    return False 
            return True 
        
        if len(s)<=1:
            return 0
            
        dp=[len(s)]*(len(s)+1); dp[0]=-1; dp[1]=0
        for i in range(1, len(s)):
            for j in range(i,-1,-1):
                if isPalin(s[j:i+1]):
                    dp[i+1]=min(dp[i+1], dp[j-1]+1)
        return dp[-1]