# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:06:48 2015

@author: ZSHU
"""
"""
the same idea of "the missing positive"
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums+=[-1]
        i, pos=0, len(nums)-1
        while i<len(nums):
            if nums[i]==-1:
                pos=i
            
            if nums[i]!=-1 and nums[i]!=i:
                temp=nums[i]
                nums[i],nums[temp]=nums[temp],nums[i]
            else:
                i+=1
        return pos
        
    

    