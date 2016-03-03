# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:55:13 2015

@author: ZSHU
"""

"""
recursive  and greedy， but too many recursive steps and over the limit  
"""
 nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
 nums=[1,2,3]
 move=0
 level=1
 res=[len(nums)]
 
 def jump(move, nums, level, res):
     
     
     if move+nums[move]>=len(nums)-1:
         if res[0]>level: res[0]=level
         return
     elif move>=len(nums) or level>=res[0] or nums[move]==0:
         return 
     else:
         temp=move
         for i in range(1, nums[move]+1):
             if nums[i+move]+i+move>temp+nums[temp]:
                 temp=i+move
         jump(temp, nums, level+1, res)
             
         
""""
Greedy, the maximum movement in every step
贪心算法，每次前移最大宽度
"""
 
  class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if len(nums)==1: return 0
        else:
            temp, move,level=0,0,1 
            while move <len(nums) and temp<len(nums) and level<len(nums):
                for i in range(0, nums[move]+1):
                    if nums[i+move]+i+move >= len(nums)-1:
                        if i==0: return level
                        else: return level+1
                    else:
                        if nums[i+move]+i+move>temp+nums[temp] and nums[i+move]!=0:
                            temp=i+move
                move=temp
                level+=1
            return None 