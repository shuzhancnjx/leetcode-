# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 09:08:01 2015

@author: ZSHU
"""

"""
TLEd 
"""
 def combine(nums, res, temp):
     if sum(temp)==target:
         temp=sorted(temp)
         if temp not in res:
             res.append(temp[:])
         return 
     else:
         for number in nums:
             if sum(temp)<target:
                 combine(nums, res, temp+[number])

"""
the following accepted after trimming some unnecessary conditioins
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combine(nums, res, target, temp):
            if target==0:
                res.append(temp)
                return 
            elif len(nums)==0:
                return 
            else:
                for i  in range( len(nums)):
                    if nums[i]<=target:
                        combine(nums[i:], res, target-nums[i],  temp+[nums[i]])
                    else:
                        return 
        
        
        candidates.sort()
        if target<candidates[0]:
            return []
        else:
            res=[]
            combine(candidates, res, target, [])
            return res 