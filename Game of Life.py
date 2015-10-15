# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:13:42 2015

@author: ZSHU
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def number(temp, board, i, j,live):
            if i<0 or j<0 or i==l or j==w: 
                return 
            else:
                if temp[i][j]!=None and temp[i][j]==1 or\
                   (temp[i][j]==None and board[i][j]==1):
                    live[0]=live[0]+1
    
        l=len(board);w=len(board[0])
        temp=[[None for i in range(w)] for j in range(l)]
        
        for i in range(l):
            for j in range(w):
                
                temp[i][j]=board[i][j]
                live=[0]
                
                number(temp, board, i-1, j, live)
                number(temp, board, i+1, j,live)
                number(temp, board, i-1, j-1, live)
                number(temp, board, i, j-1, live)
                number(temp, board, i, j+1, live)
                number(temp, board, i-1, j+1,live)
                number(temp, board, i+1, j-1, live)
                number(temp, board, i+1, j+1,live)
                
                if board[i][j]==1:
                    if live[0]<2 or live[0]>3: 
                        board[i][j]=0
                    else:
                        continue 
                else:
                    if live[0]==3:
                        board[i][j]=1
        
                
        