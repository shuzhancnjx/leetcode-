# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:29:41 2015

@author: ZSHU
"""

"""
I provided two solution: I, dynamic programming; II, recursive one (TLEd)
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
            
        res=[0]*len(nums)
        res[0]=nums[0]; res[1]=nums[1]; res[2]=nums[2]+nums[0]

        for i in range(3, len(nums)):
            res[i]=nums[i]+max(res[i-2], res[i-3])
        return max(res[-2:])


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxsum(nums, temp, res):
            if len(nums)==0:
                res.append(sum(temp))
            else:
                maxsum(nums[2:], temp+[nums[0]], res)
                maxsum(nums[3:], temp+[nums[0]], res)
        res=[]
        maxsum(nums, [], res)
        return max(res)