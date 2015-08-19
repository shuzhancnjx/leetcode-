# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:09:14 2015

@author: ZSHU
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        if n==1 or n==2:
            return True
        
        
        while n>1:
            if n%2==0:
                n=n/2
            else:
                return False
        return True
        