# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 10:26:05 2015

@author: ZSHU
"""

"""
using hash table for mapping 
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False 
        if s==t:
            return True 
            
        i=0; dic={}
        while i<len(s):
            if dic.get(s[i],None)==None:
                if t[i] in t[:i]:
                    return False 
                dic[s[i]]=t[i]        
            else:
                if dic[s[i]]!=t[i]:
                    return False 
            i+=1
        return True