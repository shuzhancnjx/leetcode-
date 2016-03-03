# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:08:47 2015

@author: ZSHU
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, p1, p2,res={}, 0,0,''
        while p2<=len(s):
            if p2<len(s) and dic.get(s[p2],None)==None:
                dic[s[p2]]=p2
            else:
                if p2-p1>len(res):
                    res=s[p1:p2]
                if p2<len(s):
                    if dic[s[p2]]+1>p1: 
                        p1=dic[s[p2]]+1
                    dic[s[p2]]=p2
            p2+=1 
        return len(res)