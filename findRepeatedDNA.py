# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:12:37 2015

@author: ZSHU
"""

"""
solution I, time limit exceeded
"""

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        
         def findrepeated(s, length):
             if len(s)<length: return None
             else:
                 res=[]
                 visited=[]
                 for i in range(0, len(s)-length):
                     if s[i:i+length] in res or  s[i:i+length] in visited:
                         continue 
                     else:
                         for j in range(i+1, len(s)):
                             if s[i:i+length]==s[j:j+length]:
                                 res+=[s[i:i+length]]
                                 break
                             else:
                                 visited+=[s[i:i+length]]
                 return res
        
         return findrepeated(s,10)