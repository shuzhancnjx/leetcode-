# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 11:42:19 2015

@author: ZSHU
"""

"""
BFS
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre=prerequisites
        numberofpre=[0 for i in xrange(numCourses)]
        preofcourses=[[] for i in xrange(numCourses)]
        
        for i in xrange(len(pre)):
            if pre[i][0] not in preofcourses[pre[i][1]]:
                numberofpre[pre[i][0]]+=1
                preofcourses[pre[i][1]].append(pre[i][0])
        res=[]; starting=[]
        for i in xrange(len(numberofpre)):
            if numberofpre[i]==0:
                starting.append(i)
        
        res+=starting
        
        while starting:
            next=starting.pop(0)
            for i in preofcourses[next]:
                numberofpre[i]-=1
                if numberofpre[i]==0:
                    starting.append(i)
                    res+=[i]
        if len(res)==numCourses:
            return res 
        return []
            