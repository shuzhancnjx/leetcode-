# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 11:26:32 2015

@author: ZSHU
"""
"""
binary search plus two 'while' loops. 
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary(nums, target):
            left, right=0, len(nums)-1
            while right>=left:
                if nums[left]==target: return left
                elif  nums[right]==target: return right
                else:
                    mid=(left+right)/2
                    if nums[mid]==target:
                        return mid
                    elif nums[mid]>target:
                        right=mid-1
                    else:
                        left=mid+1
        pos=binary(nums,target)
        if pos==None:
            return [-1, -1]
            
        left,right=pos, pos
        while left>=1 and nums[left-1]==target:
            left-=1
        while right<=len(nums)-2 and nums[right+1]==target:
            right+=1
        return [left, right]