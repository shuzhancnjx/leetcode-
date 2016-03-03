# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:26:30 2015

@author: ZSHU
"""
"""
I tried recursive at frist, but exceed time limit in the following test case
"""
 s="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
 t="bddabdcae"

 
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        
        def num(s, t, number):
            if len(t)==0 or s==t:
                number[0]+=1
                return 
            if len(s)<=len(t):
                return 
            else:
                for i in xrange(len(s)):
                    if s[i]==t[0]:
                        num(s[i+1:],t[1:],number)
        
        number=[0]
        num(s,t,number)
        return number[0]
                        
"""
the next one is dynamic programming from internet comments:

https://github.com/chaor/LeetCode_Python_Accepted
"""
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
         if s==t:
             return 1
         if len(s)<len(t):
             return 0 
         
         
         dp=[[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
         for i in range(len(dp[0])):
             dp[0][i]=1

         for i in range(1, len(dp)):
             for j in range(1, len(dp[0])):
                 if s[j-1]==t[i-1]:
                     dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
                 else:
                     dp[i][j]=dp[i][j-1]
         return dp[i][j]