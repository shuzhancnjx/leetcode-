# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:20:59 2015

@author: ZSHU
"""

"""
this is a follow-up on the remove duplicates of a sorted array. 
i add a varialbe duplicate to record the length of the repeated variable.  
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<=2:
            return len(nums)
            
        p1, p2, duplicate=0,1,1
        
        while p2<len(nums):
            if nums[p1]==nums[p2]:
                if duplicate==1: 
                    nums[p1+1]=nums[p2]; duplicate+=1; p1+=1
            elif nums[p1]!=nums[p2]:
                 nums[p1+1]=nums[p2]; duplicate=1; p1+=1
            p2+=1
        return p1+1