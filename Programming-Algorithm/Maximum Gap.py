# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:37:23 2015

@author: ZSHU
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        i,gap=1,0
        while i<len(nums):
            gap=max(gap, nums[i]-nums[i-1])
            i+=1
        return gap
            