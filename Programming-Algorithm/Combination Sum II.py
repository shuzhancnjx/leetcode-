# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 11:13:16 2015

@author: ZSHU
"""

"""
similar logic to the combination sum, but pay attention to the repeated cases
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combineii(nums, res, target, temp):
            if target==0:
                if temp not in res: res.append(temp)
                return 
            elif len(nums)==0:
                return 
            else:
                for i in range(len(nums)):
                    if nums[i]<=target:
                        combineii(nums[i+1:], res, target-nums[i], temp+[nums[i]])
                    else:
                        return 
            
        candidates.sort()
        if target<candidates[0]:
            return []
        else:
            res=[]
            combineii(candidates, res, target, [])
            return res