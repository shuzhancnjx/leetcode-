# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:32:08 2015

@author: ZSHU
"""

 class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if len(nums)==1:
            return nums[0]>=0
        else:
            i=0
            maximum=i+nums[i]
            while i<=maximum and i<len(nums):
                if i+nums[i]>=len(nums)-1:
                    return True
                else:
                    if i+nums[i]>maximum:
                        maximum=i+nums[i]
                i+=1
            return False