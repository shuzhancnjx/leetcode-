# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:26:16 2015

@author: ZSHU
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def maxarea(heights):
            heights+=[0]
            index,area,i=[],0,0
            
            while i<len(heights):
                if not index or heights[i]>=heights[index[-1]]:
                    index.append(i)
                    i+=1
                else:
                    current=index.pop()
                    area=max(area, heights[current]*(i if not index else i-index[-1]-1))
            return area

     
        if len(matrix)==0:
            return 0
        else:
            area=0
            temp1=list(matrix[0])
            for j in range(len(matrix[0])):
                temp1[j]=int(matrix[0][j]) 
            area=max(area, maxarea(temp1))    
            
            if len(matrix)==1:
                return area
       
            for i in range(1, len(matrix)):
                for j in range(len(matrix[0])):
                    temp1[j]= (0 if int(matrix[i][j])==0 else temp1[j]+1)
                area=max(area, maxarea(temp1))
            return area 