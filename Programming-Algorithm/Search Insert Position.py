# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 11:49:18 2015

@author: ZSHU
"""
'''
another application of binary search. 
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary(nums, target):
            left, right=0, len(nums)-1
            if target<nums[left]: 
                return 0
            elif target>nums[right]:
                return len(nums)
        
            while left<right:
                if nums[left]==target: 
                    return left
                elif nums[right]==target:
                    return right
                else:
                    mid=(left+right)/2
                    if target==nums[mid]:
                        return mid
                    elif target<nums[mid]:
                        right=mid-1
                    elif target>nums[mid]:
                        left=mid+1
            return left
        
        pos=binary(nums, target)
        if  pos==len(nums) or target<=nums[pos]: 
            return pos
        if target>nums[pos]:
            return pos+1