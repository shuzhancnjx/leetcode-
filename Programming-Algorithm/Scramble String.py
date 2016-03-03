# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 14:11:51 2015

@author: ZSHU
"""
 
 class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if s1==s2:
            return True 
        
        if len(s1)!=len(s2):
            return False 
        elif len(s1)==1 and s1!=s2:
            return False 
        else:
            for i in xrange(1,len(s1)):
                if set(s1[:i])==set(s2[:i]) and set(s1[i:])==set(s2[i:]):
                    if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                        return True
                if set(s1[:i])== set(s2[-i:]) and set(s1[i:])==set(s2[:-i]):
                    if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                        return True
            return False 
        
