# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 14:48:22 2015

@author: ZSHU
"""

'''
recursive + ksum
pay attention to the trimming condition

If nums[i]>0 and nums[i]>target:
    return
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def ksum(k, nums, target, res, temp):
            if k==2:
                left, right=0, len(nums)-1
                while left<right:
                    summ=nums[left]+nums[right]
                    if summ>target: right-=1
                    elif summ<target: left+=1
                    else:
                        tem= temp+[nums[left],nums[right]]
                        if tem not in res:
                            res.append(tem)
                        left+=1; right-=1
                return 
            else:
                for i in range(len(nums)-k+1):
                    if nums[i]>0 and nums[i]>target:
                        return 
                    else:
                        ksum(k-1, nums[i+1:], target-nums[i], res, temp+[nums[i]])
        
        nums.sort()
        if len(nums)<4 or (nums[0]>0 and target<nums[0]):
            return []
        else:
            res=[]
            ksum(4, nums, target, res, [])
            return res 