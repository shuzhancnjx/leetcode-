# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:08:35 2015

@author: ZSHU
"""

                       
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left=0; right=len(nums)-1
        
        while right>=left:
            if nums[left]==target or nums[right]==target:
                return True 
            else:
                center=(left+right)/2
                if nums[center]==target:
                    return True 
                else:
                    if nums[right]==nums[left]:
                        right-=1; left+=1
                    elif nums[left]>nums[right]:
                        if nums[center]>=nums[left]: 
                            if target>nums[center] or target<nums[right]:
                                left=center+1; right-=1
                            else:
                                left+=1; right=center-1
                        elif nums[center]<=nums[right]:
                            if target>nums[center] and target<nums[right]:
                                left=center+1; right-=1
                            else:
                                left+=1; right=center-1
                    else:
                        if target<nums[left] or target>nums[right]:
                            return False
                        else:
                            if target>nums[center]:
                                left=center+1; right-=1
                            else:
                                right=center-1; left+=1
        return False 
                                           
                        