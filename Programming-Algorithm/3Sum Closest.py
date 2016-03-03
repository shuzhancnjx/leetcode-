# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 12:13:46 2015

@author: ZSHU
"""

"""
1, sort the array at frist
2, two pointers scan, with the idea of binary search
3, remove the duplicates for saving compution time
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff=2**31
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            temp=target-nums[i]
            left,right=i+1, len(nums)-1
            while left<right:
                summ=nums[left]+nums[right]
                if abs(summ-temp)<diff:
                    diff=abs(summ-temp)
                    res=[nums[i],nums[left], nums[right]]
                if summ+nums[i]>target:right-=1
                if summ+nums[i]<target: left+=1
                if summ+nums[i]==target: return target
                   
        return sum(res) 