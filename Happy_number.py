# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:12:52 2015

@author: ZSHU
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        s=set()
        while n!=1 and n not in s:
            s.add(n)
            n= sum([int(x)**2 for x in str(n)])
        return n==1