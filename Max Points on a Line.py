# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:54:33 2015

@author: ZSHU
"""

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if len(points)<=2:
            return len(points)
        else:
            maxpoints=0
            for i in range(len(points)-1):
                dic={}
                repeated=0
                for j in range(i+1,len(points)):
                    if points[i].x==points[j].x and points[i].y==points[j].y:
                        if repeated==0: repeated+=2
                        else: repeated+=1
                    else:
                        if (float(points[i].x-points[j].x))==0: 
                            slope=str(points[i].x)+'xline'
                        elif (float(points[i].y-points[j].y))==0:
                            slope=str(points[i].y)+'yline'
                        else:
                            slope=(float(points[i].y-points[j].y))/(float(points[i].x-points[j].x))
                        dic[slope]=dic.get(slope,1)+1
                        
                if len(dic)>0 and repeated>0 and max(dic.values())+repeated-1>maxpoints:
                    maxpoints=max(dic.values())+repeated-1
                elif len(dic)>0 and repeated==0 and max(dic.values())>maxpoints:
                    maxpoints=max(dic.values())
                elif len(dic)==0 and repeated>maxpoints: 
                        maxpoints=repeated
                else:
                    continue 
            return maxpoints
        