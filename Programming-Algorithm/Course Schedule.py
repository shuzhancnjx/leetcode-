# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 10:50:10 2015

@author: ZSHU
"""

""
DFS + dictionary 
""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def can(dic, value, visited):
            if visited.get(value, True):
                return True
                
            visited[value]="C"
            for letter in dic[value]:
                if visited.get(letter, None)=='C' or not can(dic, letter, visited):
                        return False 
            visited[value]=True
            return True 

        dic={}; i=0; l=len(prerequisites);visited={}
        while i<l:  
            dic[prerequisites[i][1]]=dic.get(prerequisites[i][1],[])+[prerequisites[i][0]]
            visited[prerequisites[i][1]]=False
            i+=1
        
        for value in dic.keys():
            if not visited[value]:
                if not can(dic, value, visited):
                    return False 
        return True   