# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:48:30 2015

@author: ZSHU
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[0]*32;pos=31
        while n>0:
            nums[pos]=n%2
            n/=2;pos-=1

        number=0
        for i in range(len(nums)):
            number+=nums[i]*(2**i)
        return number