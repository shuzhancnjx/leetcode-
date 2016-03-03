# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:52:33 2015

@author: ZSHU
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return nums[0]
            
        p1,p2, res=0, len(nums)-1,2**31

        while p1<=p2:
            mid=(p1+p2)/2
            res=min(res, nums[p1],nums[p2],nums[mid])
            if nums[p1]==nums[p2]:
                p1+=1; p2-=1
            else:
                if nums[mid]>=nums[p1] and nums[mid]>=nums[p2]:
                    if nums[p1]>nums[p2]:
                        p1=mid+1; p2-=1
                    else:
                        p2=mid-1; p1+=1
            
                elif nums[mid]<=nums[p1] and nums[mid]<=nums[p2]:
                    if nums[p1]>nums[p2]:
                        p2=mid-1; p1+=1
                    else:
                        p1=mid+1; p2-=1
                else:
                    break
        return res