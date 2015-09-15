# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:11:12 2015

@author: ZSHU
"""

"""
the same idea about creating pascal's triangle 
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:return [1]
        if rowIndex==1:return [1,1]
        
        res=[[] for i in range(rowIndex+1)]
        res[0]=[1]; res[1]=[1,1]
        
        for i in range(2, rowIndex+1):
            for j in range(0, len(res[i-1])-1):
                res[i].append(res[i-1][j]+res[i-1][j+1])
            res[i]=[1]+res[i]+[1]
        return res[-1]

"""
the second approach in terms of saving the temporary results 
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:return [1]
        if rowIndex==1:return [1,1]
        
    
        res=[1,1]
        index=0
        while index<=rowIndex-2:
            j=0; temp=[]
            while j+1<len(res):
                temp.append(res[j]+res[j+1])
                j+=1
            res=[1]+temp+[1]; index+=1
        return res                