# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 15:13:29 2015

@author: ZSHU
"""

"""
a typical example of two pointers
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
 
        p1,p2,size=0,0,len(nums)+1
        while p2<len(nums):
            if nums[p1]>=s or nums[p2]>=s:
                return 1
            elif sum(nums[p1:p2+1])<s:
                p2+=1
            elif sum(nums[p1:p2+1])>=s:
                size=min(size, p2-p1+1)
                p1+=1
        if size>len(nums):
            return 0
        return size