# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 09:27:00 2015

@author: ZSHU
"""

"""
the one was TLEd, the second one pass the tests. the second one has two pointers
1: the first pointers points the end of the new string without repeats; and the second one was used to scan the whole
original array. 
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        i,length=1,len(nums)
        while i<length:
            if nums[i]==nums[i-1]:
                nums[i:]=nums[i+1:]+[nums[i]]
                length-=1
            i+=1
        return length


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
            
        i,j=0,1
        while j<len(nums):
            if nums[i]!=nums[j]: # not equal, then assign the number to the i+1 position 
                nums[i+1]=nums[j]
                i+=1
            j+=1

        return i+1 # the length of the new array 