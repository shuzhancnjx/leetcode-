# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:07:43 2015

@author: ZSHU
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]; dic={};n=len(nums); temp=0
        for number in nums:
            if dic.get(number, None)==None:
                dic[number]=1
            else:
                dic[number]+=1
                if dic[number]>n/3 and number not in res:
                    res+=[number]; temp+=dic[number]
                    if temp>=2*n/3:
                        return res 
        
        for value in dic.keys():
            if dic[value]> (len(nums)/3) and value not in res:
                res+=[value]
                if len(res)==3:
                    return res
        return res 