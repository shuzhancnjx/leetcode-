# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:23:17 2015

@author: ZSHU
"""

"""
still dynamic, a small change on the nums list
if starting with the first house, the exclude the last house
if starting with the second house, then include the last house
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(nums):
            if nums==[]:
                return 0
            if len(nums)<=2:
                return max(nums)
            res=[0]*len(nums); res[0]=nums[0]; res[1]=nums[1]; res[2]=nums[2]+nums[0]
            
            for i in range(3, len(nums)):
                res[i]=nums[i]+max(res[i-2], res[i-3])
            return max(res[-2:])
        
        if nums==[]:
            return 0
        return max(nums[0], nums[-1], rob(nums[1:]), rob(nums[:-1]))