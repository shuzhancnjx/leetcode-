# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:39:56 2015

@author: ZSHU
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        
        p1, p2=0, len(nums)-1
        while p1<p2:
            mid=(p1+p2)/2
            if nums[mid]==target:
                return mid
            elif nums[p1]==target:
                return p1
            elif nums[p2]==target:
                return p2
            else:
                if nums[mid]>nums[p1] and nums[mid]>nums[p2]:
                    if target>nums[p1] and target<nums[mid]:
                        p1+=1; p2=mid
                    else:
                        p1=mid; p2-=1
                elif nums[mid]<nums[p2] and nums[mid]<nums[p1]:
                    if target>nums[mid] and target<nums[p2]:
                        p1=mid; p2-=1
                    else:
                        p2=mid; p1+=1
                else:
                    if target>nums[mid]:
                        p1=mid; p2-=1
                    else:
                        p2=mid; p1+=1
        return -1            
                