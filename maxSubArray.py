# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:30:17 2015

@author: ZSHU, shuzhancnjx@gmail.com
"""

"""
return the subarray
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        
          starting, ending=0,0
          maxsofar, maxsum=nums[0],nums[0]
        
          for i in range(1, len(nums)):
             if nums[i]> maxsofar+nums[i]:
                 if nums[i]>maxsum:
                     maxsum=nums[i]
                     ending=i
                 
                 maxsofar=nums[i]
                 starting=i
               
             else:
                 if maxsofar+nums[i]>maxsum:
                     ending=i
                     maxsum=maxsofar+nums[i]
                 maxsofar+=nums[i]
                
          if starting<=ending:
              return nums[starting:ending+1]
          if starting>=ending:
              return nums[ending]



class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        
        if len(nums)==0: return None
        
        maxsofar, maxsum=nums[0],nums[0]
        
        for i in range(1, len(nums)):
            if nums[i]> maxsofar+nums[i]:
                maxsum=max(nums[i],maxsum)
                maxsofar=nums[i]
            else:
                maxsofar+=nums[i]
                maxsum=max(maxsum, maxsofar+nums[i])
                
                
        return maxsum 


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums)==0: return None
        
        maxsofar, maxsum=nums[0],nums[0]
        for i in range(1, len(nums)):
            if nums[i]> maxsofar+nums[i]:
                maxsum=max(nums[i],maxsum)
                maxsofar=nums[i]
            else:
                maxsum=max(maxsum, maxsofar+nums[i])
                maxsofar+=nums[i]
        return maxsum 