# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:43:46 2015

@author: ZSHU
"""

class solution:
    def next_permutation(nums):
        """
           purpose: I wrote a functon of next-permuation, for its smart algorithm 
           input: nums, a list of numbers 
           acknowledgement: thanks the discussions posted on internet 
           created by Zhan Shu, shuzhancnjx@gmail.com
        """
        if len(nums)<=1:
            return nums
        else: 
            point=len(nums)-1
            partition=point
            
            while point>0:
                if nums[point]<=nums[point-1]:
                    point-=1
                else:
                    partition=point-1
                    break
                
            if partition==len(nums)-1:
                return nums[::-1]
            else:
                for i in range(len(nums)-1, partition, -1):
                    if nums[i]>nums[partition]:
                        nums[partition], nums[swap]=nums[swap], nums[partition]
                        break
                nums[partition+1:]=nums[partition+1:][::-1]
                return nums 
                
        
next_permutation([6,8,7,4,3,2]) 
next_permutation([3,2,1]) 
next_permutation([1,2,3])    
next_permutation([1,1,5])   
next_permutation([1,4,5,3,2])   
  
          