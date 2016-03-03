# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:50:37 2015

@author: ZSHU
"""

"""
operation on the 2D matrix. 
1. the visited is used to record what cells have been visited 
2. a recursive function is used to visited the adjacent 1s. 
"""




class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search(i,j,grid, visited):
            if i<0 or j<0 or i>len(grid)-1 \
                or j>len(grid[0])-1 or visited[i][j]==True or grid[i][j]=='0':
                return
            else:
                visited[i][j]=True
                search(i+1,j,grid, visited)
                search(i-1,j,grid, visited)
                search(i,j-1,grid, visited)
                search(i,j+1,grid, visited)
        if grid==[]:
            return 0
             
        l=len(grid); w=len(grid[0]);number=0
        visited=[[False for i in range(w)] for j in range(l)]
 
        for i in range(l):
            for j in range(w):
                if visited[i][j]==False:
                    if grid[i][j]=='1':
                        number+=1
                        search(i,j,grid, visited)
                    else:
                        visited[i][j]=True
        return number 