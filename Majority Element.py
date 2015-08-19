# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:56:15 2015

@author: ZSHU
"""

"""
Hash table or dictionary 
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        
        dic={}
        for number in nums:
            dic[number]=dic.get(number,0)+1
            if dic[number]>(len(nums)/2):
                return number 
        