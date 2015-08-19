# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:23:11 2015

@author: ZSHU
"""

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        
        res, temp, i=[], [str(nums[0])],1
        while i<=len(nums):
            if i==len(nums) or nums[i-1]+1!=nums[i]:
                temp.append(str(nums[i-1]))
                if temp[0]!=temp[1]:
                    res.append("->".join(temp))
                else:
                    res.append(temp[0])
                if i!=len(nums):
                    temp=[str(nums[i])]
            i+=1
        return res 