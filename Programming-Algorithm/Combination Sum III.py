# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:55:05 2015

@author: ZSHU
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums=range(1,10)
        
        def combine(res, nums, height, temp):
            if sum(temp)>n or len(temp)>k:
                return 
            elif sum(temp)==n and len(temp)==k:
                res.append(temp)
                return 
            else:
                for i in range(len(nums)):
                    combine(res, nums[i+1:], height+1, temp+[nums[i]])
        res=[]
        combine(res, nums, 0, [])
        return res 