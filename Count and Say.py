# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 08:52:34 2015

@author: ZSHU
"""
"""
recursive algorithm
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count(s):
            i, count,res=1,1,''
            while i<=len(s):
                if i<len(s) and s[i]==s[i-1]:
                    count+=1      
                else:
                    res+=str(count)+s[i-1]
                    count=1
                i+=1
            return res 

        def say(n, depth, temp):
            if depth==n:
                return temp
            else:
                return countsay(n,depth+1, count(temp))
                
        return say(n,1,'1')