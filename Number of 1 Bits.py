# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:26:53 2015

@author: ZSHU
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[0]*32;pos=0
        while n>0:
            nums[pos]=n%2
            n/=2; pos+=1
        return sum(nums)