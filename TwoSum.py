# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:15:07 2015

@author: ZSHU
"""

nums=[8,7,9]
target=-8
twosums(nums, target)

"""
this one is too long....

"""
 def twosums(nums, target):
     if len(nums)==0:
         return None 
     elif len(nums)==1 and nums[0]==target:
         return {'index1':0, 'index2':0}
     else:
        lookup={}
        for i in range(len(nums)):
             lookup[nums[i]]=lookup.get(nums[i],[])+[i]
        
        nums.sort()
        index1, index2 =0, len(nums)-1    
        
        while index2>index1:
            if nums[index1]+nums[index2]==target:
                if len(lookup[nums[index1]])>1:
                    index1=lookup[nums[index1]][0]
                    lookup[nums[index1]].remove(lookup[nums[index1]][0])
                else:
                    index1=lookup[nums[index1]][0]
                if len(lookup[nums[index2]])>1:
                    index2=lookup[nums[index2]][0]
                    lookup[nums[index2]].remove(lookup[nums[index2]][0])
                else:
                    index2= lookup[nums[index2]][0]
                if index2<index1:
                    index2, index1=index1, index2
                return (index1+1, index2+1)
                
            elif nums[index1]+nums[index2]>target:
                index2-=1
            else:
                index1+=1

class Solution:
     """
        this code was based on the idea: http://www.cnblogs.com/zuoyuan/p/3698966.html
        short and clean
     """
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        """
        this code was based on the idea: http://www.cnblogs.com/zuoyuan/p/3698966.html
        short and clean
        """
        dict={}
        for i in range(len(nums)):
            x=nums[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x]=i