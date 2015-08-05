# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 12:22:22 2015

@author: ZSHU
"""

"""
The basic logic of the solution is the sweepline algorithm. the variable active is to save all the
active heights. 
Note: the variable points is to save all the left and right points. I also borrow the idea of using 
positive and negative signes to distinguish the left point from the right point. 
"""

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if len(buildings)==0: return []
        if len(buildings)==1: return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
            
        points=[]
        for building in buildings:
            points+=[[building[0],building[2]]]
            points+=[[building[1],-building[2]]]
        points=sorted(points, key=lambda x: x[0])
        
        moving, active, res, current=0, [0], [],-1
       
        while moving<len(points):
            i=moving
            while i<=len(points):
                if i<len(points) and points[i][0]==points[moving][0]:
                    if points[i][1]>0:
                        active+=[points[i][1]]
                        if points[i][1]>current:
                            current=points[i][1]
                            if len(res)>0 and res[-1][0]==points[i][0]: 
                                res[-1][1]=current
                            else:
                                res+=[[points[moving][0], current]]
                    else:
                        active.remove(-points[i][1])
                    i+=1
                else:
                    break
            if max(active)<current:
                current=max(active)
                res+=[[points[moving][0], current]] 
            moving=i
        return res 
        
        
"""
some testing cases from leetcode
"""     
        
 buildings=[ [1,2,1], [1,2,2],  [1,2,3] ]
 buildings= [[1,10001,10000],[2,10001,9999],[3,10001,9998],[4,10001,9997],[5,10001,9996],[6,10001,9995]  ] 
 buildings=[ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ] 
 buildings=[[0,2,3],[2,5,3]]
 buildings=[[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]
        
        
 
                    
                    
            
            
        
        
        
        
        
        

      
         
     