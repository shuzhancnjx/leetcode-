# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:21:15 2015

@author: ZSHU
"""

"""
a smart algorithm from internet 
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output=[1]*len(nums); p1,p2=1,1
 
        for i in range(1, len(nums)):
            p1*=nums[i-1]
            output[i]*=p1
 
        for i in range(len(nums)-2, -1,-1):
            p2*=nums[i+1]
            output[i]*=p2
        
        return output 