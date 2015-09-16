# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:22:43 2015

@author: ZSHU
"""

"""
logically, this is not a difficult one, but a lot of corner cases: 
1. I designed a matrix 'dp' to dp record the status of individual cell 
   only True in the dp means that 'O' will be kept in board 

2. start with the cell in the boarders 
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def search(i,j,board, dp):
            if i<=0 or j<=0 or i>=l-1 or j>=w-1 or board[i][j]=='X' or dp[i][j]==True:
                 return 
            else:
                dp[i][j]=True
                search(i+1, j, board, dp)
                search(i-1, j, board, dp)
                search(i, j-1, board, dp)
                search(i, j+1, board, dp)
        
        if board==[] or len(board)<=1 or len(board[0])<=1:
            return 
        
        l=len(board); w=len(board[0])
        dp= [[False for i in range(w)] for j in range(l)]
        for k in range(1, w-1):
            if board[0][k]=='O':
                search(1, k, board, dp)
            if board[l-1][k]=='O':
                search(l-2, k, board, dp)
         
        for k in range(1, l-1):
            if board[k][0]=='O':
                search(k,1,board, dp)
            if board[k][w-1]=='O':
                search(k,w-2,board,dp)
 
        for i in range(1,l-1):
            board[i]=list(board[i])
            for j in range(1,w-1):
                if dp[i][j]==False and board[i][j]=='O':
                    board[i][j]='X'
            board[i]=''.join(board[i])
        return 