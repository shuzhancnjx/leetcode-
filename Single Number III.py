# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:07:23 2015

@author: ZSHU
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}; res=[]
        for number in nums:
            if dic.get(number,None)==None:
                dic[number]=1
            else: 
                dic[number]+=1
        for value in dic.keys():
            if dic[value]==1:
                res+=[value]
                if len(res)==2:
                    return res 