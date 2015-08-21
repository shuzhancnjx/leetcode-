# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:03:56 2015

@author: ZSHU
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if val not in nums:
            return len(nums)
        else:
            i,length=0,len(nums)
            while i<length:
                if nums[i]==val:
                    nums[i],nums[length-1]=nums[length-1],nums[i]
                    length-=1
                    i-=1
                i+=1
            return length