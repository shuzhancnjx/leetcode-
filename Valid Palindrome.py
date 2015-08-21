# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:07:39 2015

@author: ZSHU
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s=s.lower()
        l, r=0, len(s)-1
        
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while  r>l and not s[r].isalnum():
                r-=1
            
            if s[l]!=s[r]:
                return False 
            else:
                l+=1
                r-=1
        return True 