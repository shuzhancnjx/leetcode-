# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:04:47 2015

@author: ZSHU
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1=p2=0

        while p1<len(nums) and p2<len(nums):
            if nums[p1]==0:
                p2=p1+1
                while p2<len(nums) and nums[p2]==0:
                    p2+=1
                if p2<len(nums): nums[p1],nums[p2]=nums[p2],nums[p1]
            else:
                p1+=1