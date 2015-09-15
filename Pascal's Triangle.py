# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:00:18 2015

@author: ZSHU
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res=[[1], [1,1]]
        if numRows<=2:
            return res[:numRows]
        
        for i in range(2,numRows):
            j=0; temp=[1]
            while j+1<len(res[i-1]):
                temp.append(res[i-1][j]+res[i-1][j+1])
                j+=1
            res.append(temp+[1])
        return res 