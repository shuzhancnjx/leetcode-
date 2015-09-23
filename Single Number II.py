# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:55:22 2015

@author: ZSHU
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}; A=nums
        for i in range(len(A)):
            if A[i] not in dict:
                dict[A[i]] = 1
            else:
                dict[A[i]] += 1
        for word in dict:
            if dict[word] == 1:
                return word