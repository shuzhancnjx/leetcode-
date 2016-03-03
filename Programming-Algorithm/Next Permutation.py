# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 09:14:16 2015

@author: ZSHU
"""
"""
this real challenge is that it requires the in-place manipulation... 
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return 
       
        pos,right, i=None, len(nums)-2, len(nums)-1
        while right>=0:
            if right==0 or nums[right]<nums[right+1]:
                break 
            right-=1
         
        if right==0 and nums[right]>=nums[right+1]:
            while i>right:
                nums[right],nums[i]=nums[i],nums[right]
                i-=1; right+=1
            return 
        else:
            while i>right:
                if nums[i]>nums[right]:
                    nums[right], nums[i]=nums[i],nums[right]
                    break 
                i-=1
       
            i, right=len(nums)-1, right+1
            while i>right:
                nums[right],nums[i]=nums[i],nums[right]
                i-=1; right+=1
            return 
            
            
            
            
            