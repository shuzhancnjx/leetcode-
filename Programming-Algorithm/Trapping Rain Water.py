# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:37:29 2015

@author: ZSHU
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=2:
            return 0
        
        water=0
        left=[height[0]]*len(height)
        right=[height[len(height)-1]]*len(height)

        for i in range(1, len(height)):
            left[i]=max(left[i-1], height[i])

        for i in range(len(height)-2,-1,-1):
            right[i]=max(right[i+1],height[i])
            water+=min(right[i],left[i])-height[i]
        return water
    
    