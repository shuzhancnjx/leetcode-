# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:33:47 2015

@author: ZSHU
"""
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if len(nums)>=2:
            left, right=0, len(nums)-1
        
            while left<len(nums) and nums[left]==0:
                left+=1
            while right>=0 and nums[right]==2:
                right-=1
        
            point=left
            while point<=right:
                if nums[point]==0 and point>left:
                    nums[left],nums[point]= nums[point],nums[left]
                    left+=1
                elif nums[point]==2:
                    nums[right],nums[point]= nums[point],nums[right]
                    right-=1
                else:
                    point+=1
            