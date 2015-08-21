# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:49:30 2015

@author: ZSHU
"""
"""
time limit exceed. 
"""
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        
        def ispalindrome(s):
            p1,p2=0,len(s)-1
            while p1<=p2:
                if s[p1]==s[p2]:
                    p1+=1
                    p2-=1
                else:
                    return False 
            return True 
        
        
        if len(s)<=1:
            return s
            
        pos=0
        for i in range(len(s),-1,-1):
            if ispalindrome(s[:i]):
                pos=i
                break 
        
        return s[pos:][::-1]+s

"""
using BMP algorithm as comments from: 
http://bookshadow.com/weblog/2015/05/22/leetcode-shortest-palindrome/

"""

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if len(s)<=1:
            return s
        rev=s[::-1]
        new=s+"*"+rev
        dp=[0 for i in range(len(new))]
        
        for i in range(1, len(new)):
            j=dp[i-1]
            while j>0 and new[i]!=new[j]:
                j=dp[j-1]
            dp[i]=j+(new[i]==new[j])
        
        return rev[:-dp[-1]]+s
       