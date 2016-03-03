# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:29:54 2015

@author: ZSHU
"""
"""
i tried without the breakable function to cut the recursive trees, and it exceeded the
time limit in the following testing case, and so i add a function to test if a word can be broke into 
the words given the dictionary. 
"""
 
 s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
 wordDict =["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        
        def breakable(s):
            dp=[False for i in range(len(s)+1)]
            dp[0]=True 
            
            for i in range(len(s)):
                for j in range(i+1):
                    if dp[j] and s[j:i+1] in wordDict:
                        dp[i+1]=True 
            return dp[-1]
            
        def breakword(s, temp, res):
            if len(s)==0:
                res.append(' '.join(temp))
                return 
            else:
                for i in range(len(s)):
                    if s[:i+1] in wordDict and breakable(s[i+1:]):
                        breakword(s[i+1:],temp+[s[:i+1]],res)
        
        res=[]
        temp=[]
        breakword(s, temp, res)
        return res 

