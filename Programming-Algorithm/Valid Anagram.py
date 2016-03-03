# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:56:22 2015

@author: ZSHU
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s)!=len(t) or set(s)!=set(t):
            return False 
        dic1={}
        dic2={}
        for i in range(len(s)):
            dic1[s[i]]=dic1.get(s[i],0)+1
            dic2[t[i]]=dic2.get(t[i],0)+1
        return dic1==dic2