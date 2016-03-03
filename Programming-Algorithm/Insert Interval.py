# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 12:20:44 2015

@author: ZSHU
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        
        def insertnew(newIntervals, intervals):
            if len(intervals)==0:
                return [newIntervals]
            if newIntervals==[]:
                return intervals 
            p1=0
            while p1<len(intervals):
                if newIntervals.start<intervals[p1].start:
                    if newIntervals.end<intervals[p1].start:
                        return intervals[:p1]+[newIntervals]+intervals[p1:]
                    res=merge([newIntervals]+intervals[p1:])
                    return intervals[:p1]+res
                elif newIntervals.start>=intervals[p1].start \
                    and newIntervals.start<=intervals[p1].end:
                    if newIntervals.end<=intervals[p1].end:
                        return intervals 
                    else:
                        intervals[p1].end=newIntervals.end
                        return intervals[:p1]+merge(intervals[p1:])
                else:
                    if p1==len(intervals)-1:
                        return intervals+[newIntervals]
                p1+=1
        
        def merge(intervals):
            if len(intervals)<=1: return intervals
            p1, p2=0,1
            result=[]
            while p1<len(intervals) and p2<len(intervals):
                if intervals[p1].end>=intervals[p2].start and intervals[p1].end<=intervals[p2].end:
                    intervals[p1].end=intervals[p2].end
                    if p2==len(intervals)-1: result+=[intervals[p1]]
                elif intervals[p1].end< intervals[p2].start:
                    if p2==len(intervals)-1:
                        result+=[intervals[p1],intervals[p2]]
                    else:
                        result+=[intervals[p1]]
                    p1=p2
                else:
                    if p2==len(intervals)-1 and intervals[p1] not in result:
                        result+=[intervals[p1]]
                p2+=1
            return result
            
        return insertnew(newInterval, intervals)   