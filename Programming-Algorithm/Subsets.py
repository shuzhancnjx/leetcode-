# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:00:00 2015

@author: ZSHU
"""

'''
another typical example of recursive algorithm 
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def combine(length, vector, temp, res):
            if len(temp)==length:
                res.append(temp); return 
            elif len(vector)==0:
                return 
            else:
                for i in range(len(vector)):
                    combine(length, vector[i+1:], temp+[vector[i]], res)
        res=[]; nums.sort()
        for length in range(len(nums)+1):
            combine(length, nums, [], res)
        return res 