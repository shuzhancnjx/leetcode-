# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 11:01:12 2015

@author: ZSHU
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if len(intervals)==None: return []
        if len(intervals)==1: return intervals 
        
        result=[]
        temp= sorted(intervals, key=lambda x:x.start)
        i,j=0,1
        
        while i <len(temp) and j<len(temp):
            if temp[i].end>=temp[j].start and temp[i].end<=temp[j].end:
                temp[i].end=temp[j].end
                if j==len(temp)-1:
                    result+=[temp[i]]
            
            elif temp[i].end< temp[j].start:
                if j==len(temp)-1:
                    result+=[temp[i],temp[j]]
                else:
                    result+=[temp[i]]
                i=j
            else:
                if j==len(temp)-1 and temp[i] not in result:
                    result+=[temp[i]]
            
            j+=1   
                
        return result