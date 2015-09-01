# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 09:39:26 2015

@author: ZSHU
"""

"""
my first version 
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table={'I':1,'IV':4,'V':5,'IX':9,'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400,'D':500, 'CM':900,'M':1000}
        if len(s)==1:
            return table[s[0]]
            
        i,num=1,0
        while i<len(s):
            if table[s[i-1]]>=table[s[i]]:
                num+=table[s[i-1]]; i+=1
                if i==len(s):
                    num+=table[s[i-1]]
            else:
                num+=table[s[i-1:i+1]]; i+=2
                if i-1==len(s)-1: num+=table[s[i-1]]
        return num   

"""
the second version from http://www.cnblogs.com/zuoyuan/p/3779688.html
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table={'I':1,'IV':4,'V':5,'IX':9,'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400,'D':500, 'CM':900,'M':1000}
        if len(s)==1:
            return table[s[0]]
            
        i,num=1,0
        while i<len(s):
            if table[s[i-1]]>=table[s[i]]:
                num+=table[s[i-1]]; i+=1
                if i==len(s):
                    num+=table[s[i-1]]
            else:
                num+=table[s[i-1:i+1]]; i+=2
                if i-1==len(s)-1: num+=table[s[i-1]]
        return num  