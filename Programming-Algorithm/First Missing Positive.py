# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:05:32 2015

@author: ZSHU
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if len(nums)==0: return 1

        i=0
        while i<len(nums):
            if nums[i]<=0:
                i+=1
            elif nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                temp=nums[i]-1
                nums[i],nums[temp]=nums[temp],nums[i]
            else:
                i+=1
        
        for i in xrange(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1